# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-09-20 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreditCard', '0006_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categoryId',
        ),
        migrations.AddField(
            model_name='product',
            name='categoryId',
            field=models.ManyToManyField(to='CreditCard.category'),
        ),
    ]
