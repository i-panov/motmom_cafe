import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from urllib.parse import unquote_plus

from django.views.decorators.http import require_POST

from cafe.models import Product
from .models import Order, OrderItem


def profile(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, 'accounts/profile.html', {
        'orders': orders,
        'sum': sum(o.sum for o in orders if o.completed)
    })


def statistics(request):
    orders = list(Order.objects.all())
    # years = [o. for o in orders]

    result = {
        'years': {
            'year': 2017,
            'employees': [
                {
                    'name': 'Tom',
                    'months': [100, 200]
                }
            ]
        }
    }

    return render(request, 'accounts/statistics.html')


@require_POST
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


def order(request):
    token = request.GET.get('token')
    current = Order.from_token(token)

    if not request.user.is_superuser and request.user != current.user:
        redirect('/')

    return render(request, 'accounts/order.html')


def set_order_status(request):
    order = Order.objects.get(pk=request.POST['id'])
    order.completed = request.POST['status']
    order.save()
