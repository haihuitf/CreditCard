# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-24 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='content_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='content_count',
            field=models.IntegerField(default=0),
        ),
    ]
