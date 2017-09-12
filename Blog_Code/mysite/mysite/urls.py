"""mysite URL Configuration

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
from django.conf.urls import patterns, include, url
from blog.views import *
from blog.models import *
admin.site.register([Category,Tag,Blog])
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^index/$', 'blog.views.index'),
    url(r'^blogs/$',get_blogs),
    url(r'^detail/(\d+)/$',get_details ,name='blog_get_detail'),
    url(r'^write/$',get_write),
    url(r'^$', login, name='login'),
    url(r'^login/$',login,name = 'login'),
    url(r'^regist/$',regist,name = 'regist'),
    url(r'^index/$',index,name = 'index'),
    url(r'^logout/$',logout,name = 'logout'),
    url(r'^test/',test,name='test'),
    #url(r'^blog/', include('blog.urls')),
]