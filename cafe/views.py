# coding: utf-8

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

import json

from django.views.generic import TemplateView, DetailView, ListView, RedirectView

from .models import Category, Product


MOST_POPULAR_CATEGORY = Category(id='', name='Самое популярное')


class MenuView(DetailView):
    template_name = 'cafe/menu.html'
    model = Category
    context_object_name = 'checked_category'

    categories = Category.objects.all()

    def get_object(self, queryset=None):
        return MOST_POPULAR_CATEGORY

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['categories'] = [MOST_POPULAR_CATEGORY] + list(self.categories)
        return context


class MostPopularView(MenuView):
    def get_context_data(self, **kwargs):
        context = super(MostPopularView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.order_by('-purchases_count')[:5]
        return context


class CategoryView(MenuView):
    def get_object(self, queryset=None):
        return next(cat for cat in self.categories if cat.id == int(self.kwargs['pk']))

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['products'] = self.get_object().product_set.all()
        return context


class RenderCartView(ListView):
    template_name = 'cafe/cart.html'
    http_method_names = ['post']
    context_object_name = 'products'
    model = Product

    def get_queryset(self):
        products = json.loads(self.request.POST['products'])
        return Product.objects.filter(pk__in=products)

    def post(self, request):
        return self.get(request)
