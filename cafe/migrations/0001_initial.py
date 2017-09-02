# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
            ],
            options={
                'db_table': 'category',
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('preview', models.ImageField(upload_to='')),
                ('purchases_count', models.IntegerField(verbose_name='Количество покупок')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.Category')),
            ],
            options={
                'db_table': 'product',
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
