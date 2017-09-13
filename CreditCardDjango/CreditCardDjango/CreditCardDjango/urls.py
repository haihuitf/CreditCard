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
from django.conf.urls import include
from CreditCard.views import login
from CreditCard.views import regist, change_pwd, addCategory, modifyCategory
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # ��¼
    url(r'^login/', login,name='login'),
    # ע��
    url(r'^regist/', regist,name='regist'),
    # �޸�����
    url(r'^change/', change_pwd,name='change_pwd'),
    # ��ӷ���
    url(r'^category/', addCategory,name='addCategory'),
    # �޸ķ���
    url(r'^modifyCategory/', modifyCategory, name='modifyCategory')
]
