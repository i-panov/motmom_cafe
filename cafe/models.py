# coding: utf-8

from __future__ import unicode_literals
from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField('Название', max_length=20)
    description = models.CharField('Описание', max_length=200)
    preview = models.ImageField()    
    purchases_count = models.IntegerField('Количество покупок')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
