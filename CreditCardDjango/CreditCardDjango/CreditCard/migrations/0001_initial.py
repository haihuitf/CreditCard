# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-09-11 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cardno', models.IntegerField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('owener', models.CharField(max_length=150)),
                ('credTotla', models.DecimalField(decimal_places=3, max_digits=19)),
                ('creditBalance', models.DecimalField(decimal_places=3, max_digits=19)),
                ('dayRate', models.FloatField()),
                ('freeRate', models.FloatField()),
                ('frozenStatus', models.IntegerField(default=0)),
                ('createTime', models.DateField(auto_now=True)),
                ('updateTime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='saleorder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productList', models.CharField(max_length=150)),
                ('cost', models.FloatField()),
                ('createTime', models.DateField(auto_now=True)),
                ('updateTime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='shoppingHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('cost', models.FloatField()),
                ('serno', models.IntegerField()),
                ('detail', models.CharField(max_length=150)),
                ('createTime', models.DateField(auto_now=True)),
                ('updateTime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='transactionBill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payfor', models.FloatField()),
                ('cost', models.FloatField()),
                ('serialno', models.IntegerField()),
                ('createTime', models.DateField(auto_now=True)),
                ('updateTime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=1500)),
                ('mobile', models.CharField(max_length=150)),
                ('islocked', models.IntegerField(default=0)),
                ('bindcard', models.IntegerField(max_length=150)),
                ('role', models.IntegerField(default=0)),
                ('isdel', models.IntegerField(default=0)),
                ('createTime', models.DateField(auto_now=True)),
                ('updateTime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='shoppinghistory',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreditCard.UserInfo'),
        ),
        migrations.AddField(
            model_name='saleorder',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreditCard.UserInfo'),
        ),
        migrations.AddField(
            model_name='cardinfo',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreditCard.UserInfo'),
        ),
    ]
