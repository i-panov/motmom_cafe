import json
from itertools import groupby

from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView, RedirectView

from cafe.models import Product
from .models import Order, OrderItem


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'accounts/profile.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['sum'] = sum(o.sum for o in self.get_queryset() if o.completed)
        return context


class StatsView(UserPassesTestMixin, DetailView):
    template_name = 'accounts/stats.html'
    context_object_name = 'stat_items'

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        year = self.request.GET['year']
        month = self.request.GET['month']
        return Order.objects.filter(completed=True, date__year=year, date__month=month)

    def get_object(self, queryset=None):
        groups = groupby(self.get_queryset(), lambda o: o.user)
        return [{'user': user, 'sum': sum(o.sum for o in orders)} for user, orders in groups]

    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)
        context['year'] = self.request.GET['year']
        context['month'] = self.request.GET['month']
        return context


@require_POST
@login_required
def add_order(request):
    cart = json.loads(request.POST['cart'])
    order = Order(user=request.user)
    order.save()

    for pk, count in cart.items():
        if count > 0:
            item = OrderItem(order=order, product=Product.objects.get(pk=pk), count=count)
            item.save()

            order.orderitem_set.add(item)

    order.save()
    return JsonResponse({'status': 'success'})


class OrderView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/order.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['order_items'] = list(self.get_object().orderitem_set.all())
        return context


class CheckOrderView(RedirectView):
    http_method_names = ['post']

    def get_redirect_url(self, *args, **kwargs):
        request = self.request
        token = request.POST.get('token')
        order = Order.from_token(token)

        if request.user == order.user or request.user.is_superuser:
            return reverse('accounts:order', args=(order.pk,))
        else:
            return reverse('cafe:most_popular')


@require_POST
@user_passes_test(lambda u: u.is_superuser)
def set_order_status(request):
    order = Order.objects.get(pk=request.POST['pk'])
    order.completed = request.POST['status']
    order.save()
    return JsonResponse({'status': 'success'})
