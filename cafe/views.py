# coding: utf-8

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

import json

from .models import Category, Product

MOST_POPULAR_CATEGORY = Category(id='', name='Самое популярное')


def render_menu(request, categories, checked_category, products):
    return render(request, 'cafe/menu.html', {
        'categories': [MOST_POPULAR_CATEGORY] + list(categories),
        'checked_category': checked_category,
        'products': products,
        'user': request.user
    })


@login_required
def most_popular(request):
    categories = Category.objects.all()
    checked_category = MOST_POPULAR_CATEGORY
    products = Product.objects.order_by('-purchases_count')[:5]
    return render_menu(request, categories, checked_category, products)


@login_required
def category(request, pk):
    categories = Category.objects.all()
    checked_category = next(cat for cat in categories if cat.id == int(pk))
    products = checked_category.product_set.all()
    return render_menu(request, categories, checked_category, products)


@login_required
@require_POST
def render_cart(request):
    data = json.loads(request.POST['cart'])
    products = {Product.objects.get(pk=pk): count for pk, count in data.items()}
    return render(request, 'cafe/cart.html', {'products': products})
