from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    exclude = [ 'purchases_count' ]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
