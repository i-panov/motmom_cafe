# coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from .models import Category, Product


MOST_POPULAR_CATEGORY = Category(name='Самое популярное')


@login_required
def getMostPopular(request):
    return render(request, 'cafe/menu.html', {
        'categories': [ MOST_POPULAR_CATEGORY ] + list(Category.objects.all()),
        'checked_category': MOST_POPULAR_CATEGORY,
        'products': Product.objects.order_by('-purchases_count')[:5]
    })


@login_required
def getCategory(request, pk):
    categories = [ MOST_POPULAR_CATEGORY ] + list(Category.objects.all())
    checked_category = next(cat for cat in categories if cat.id == int(pk))

    return render(request, 'cafe/menu.html', {
        'categories': categories,
        'checked_category': checked_category,
        'products': checked_category.product_set.all()
    })
