# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-24 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20161024_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='content_count',
        ),
        migrations.AddField(
            model_name='blog',
            name='content_count',
            field=models.IntegerField(default=0),
        ),
    ]
