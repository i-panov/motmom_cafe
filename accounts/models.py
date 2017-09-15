from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, F
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from base64 import b64encode, b64decode

from cafe.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата', auto_now_add=True)
    completed = models.BooleanField('Выполнено', default=False)

    @property
    def sum(self):
        return sum([item.product.price * item.count for item in self.orderitem_set.all()])
        # return self.orderitem_set.aggregate(sum=Sum(F('product.price') * F('count')))

    @property
    def token(self):
        token = '%s#%s' % (self.date, self.pk)
        return b64encode(bytes(token, 'utf-8')).decode()

    @staticmethod
    def from_token(token):
        date, pk = b64decode(bytes(token, 'utf-8')).decode().split('#')
        return get_object_or_404(Order, pk=pk, date=date)

    def __str__(self):
        date_str = self.date.astimezone().strftime('%d/%m/%y %H:%M:%S')
        return '%s, %s, %s, %s' % (self.user, date_str, self.sum, self.completed)

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField('Количество', default=1)

    def __str__(self):
        return '%s, %s, %s' % (self.order.pk, self.product, self.count)

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'
