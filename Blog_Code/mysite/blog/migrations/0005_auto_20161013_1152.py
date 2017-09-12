# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-13 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161012_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='\u6807\u9898')),
                ('author', models.CharField(max_length=16, verbose_name='\u4f5c\u8005')),
                ('content', models.TextField(verbose_name='\u535a\u5ba2\u6b63\u6587')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_modify_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='\u79f0\u547c')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('content', models.CharField(max_length=240, verbose_name='\u5185\u5bb9')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog', verbose_name='\u535a\u5ba2')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='\u540d\u79f0')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_modify_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]
