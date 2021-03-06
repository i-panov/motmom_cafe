# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(upload_to='products', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchases_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество покупок'),
        ),
    ]
