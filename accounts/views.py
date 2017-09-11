from django.shortcuts import render, redirect
from urllib.parse import unquote_plus

from .models import Order


def profile(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, 'accounts/profile.html', {
        'orders': orders,
        'sum': sum(o.sum for o in orders),
        'user': request.user
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
