#coding:UTF-8
from django.shortcuts import render,render_to_response
from CreditCardDjango import settings
from django.http import HttpResponseRedirect
from .forms import UserForm,RegistForm
from .models import UserInfo
from django.template import RequestContext
# Create your views here.

#TEST
def index(request):
    return HttpResponseRedirect("Hello,world")

#用户登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = UserInfo.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/online/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(request))

def regist(request):
    if request.method == "POST":
        uf = RegistForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            name = uf.cleaned_data['name']
            mobile = uf.cleaned_data['mobile']
            bindcard = uf.cleaned_data['bindcard']
            # 将表单写入数据库
            user = UserInfo()
            user.username = username
            user.password = password
            user.mobile = mobile
            user.name = name
            user.bindcard = bindcard
            user.save()
            return render_to_response('regist.html', {"username":username}, context_instance=RequestContext(request))
    else:
        uf = RegistForm()
    return render_to_response("login.html", {'uf': uf}, context_instance=RequestContext(request))


