# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-09-11 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreditCard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardinfo',
            name='cardno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='bindcard',
            field=models.IntegerField(),
        ),
    ]
