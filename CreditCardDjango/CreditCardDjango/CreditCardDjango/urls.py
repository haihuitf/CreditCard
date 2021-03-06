"""CreditCardDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from CreditCard.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 登录
    url(r'^login/', login,name='login'),
    # 注册
    url(r'^regist/', regist,name='regist'),
    # 修改密码
    url(r'^change/', change_pwd,name='change_pwd'),
    # 添加分类
    url(r'^category/', addCategory,name='addCategory'),
    # 修改分类
    url(r'^modifyCategory/', modifyCategory, name='modifyCategory'),
    # 添加商品
    url(r'^addProduct/', addProduct, name='addProduct'),
    # 修改商品
    url(r'^modifyProduct/', modifyProduct, name='modifyProduct'),
    # 商品列表
    url(r'^productList/', productList, name='productList'),

    url(r'^ProductDetail/', ProductDetails, name='ProductDetail')
]
