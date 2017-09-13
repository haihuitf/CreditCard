#coding:UTF-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm, RegistForm, ChangePwdForm, addCategoryForm, modifyCategoryForm
from .models import UserInfo, CardInfo, category
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
# Create your views here.

#TEST
def index(request):
    return HttpResponseRedirect("Hello,world")

# 登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 提交表单
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 是否存在用户
            user = UserInfo.objects.filter(username__exact = username,password__exact = password)
            if user:
                for us in user:
                    # 用户的状态是否为0(1:删除)
                    if us.isdel == 0:
                        # 用户是否被锁定(1:锁定)
                        if us.islocked == 0:
                            response = HttpResponse("success")
                            response.set_cookie('username',username,3600)
                            return response
                        # response = HttpResponseRedirect('login/')
                        else:
                            return HttpResponse("你的用户被锁定")
                    else:
                        return HttpResponse('你的用户状态为删除')
            else:
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(request))

# 注册
def regist(request):
    if request.method == "POST":
        uf = RegistForm(request.POST)
        if uf.is_valid():
            # 获取表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            name = uf.cleaned_data['name']
            mobile = uf.cleaned_data['mobile']
            bindcard = uf.cleaned_data['bindcard']
            user = UserInfo.objects.filter(username__exact = username)
            if len(user) == 0:
                # 提交表单存入数据库
                user = UserInfo()
                user.username = username
                user.password = password
                user.mobile = mobile
                user.name = name
                user.bindcard = bindcard
                user.save()
                # 注册的同时生成一张信用卡
                userId_id = user.id
                CardInfo.objects.get_or_create(
                    userId_id = userId_id,
                    cardno = bindcard,
                    password = "123456",
                    owener = username,
                    credTotla = 10000,
                    creditBalance = 5000,
                    dayRate = 0.03,
                    freeRate = 0.03
                )
            else:
                return HttpResponse("用户名已经存在")
            return render_to_response('regist.html', {"username":username}, context_instance=RequestContext(request))
    else:
        uf = RegistForm()
    return render_to_response("login.html", {'uf': uf}, context_instance=RequestContext(request))

# 编辑用户信息
# @login_required表示登录状态才会调用此模块
@login_required
def myview(request):
    return render_to_response('index.html')
# def edit_user(request):
#     if request.method == "POST":
#         uf = UserForm()
#         if uf.is_valid():
#             password = uf.cleaned_data['password']
#             name = uf.cleaned_data['name']
#             mobile = uf.cleaned_data['mobile']
#             bindcard = uf.cleaned_data['bindcard']
#             return

# 修改密码
def change_pwd(request):
    if request.method == "POST":
        uf = ChangePwdForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            old_password = uf.cleaned_data['old_password']
            new_password = uf.cleaned_data['new_password']
            # 判断用户原密码是否匹配
            user = UserInfo.objects.filter(username = username)
            if user:
                passwd = UserInfo.objects.filter(username=username,password=old_password)
                if passwd:
                    UserInfo.objects.filter(username=username,password=old_password).update(password=new_password)
                    info = '密码修改成功!'
                else:
                    info = "请'检查原密码是否输入正确"
            elif len(user)==0:
                info = "请检查输入的用户是否正确"
        return HttpResponse(info)
    else:
        uf = ChangePwdForm()
    return render_to_response('change.html', {'uf':uf}, context_instance=RequestContext(request))

# 商品分类
def addCategory(request):
    if request.method == "POST":
        uf = addCategoryForm(request.POST)
        if uf.is_valid():
            name = uf.cleaned_data['name']
            qcategory = category.objects.filter(name = name)
            # 分类名称不能重复
            if len(qcategory) == 0:
                cate = category()
                cate.name = name
                cate.save()
                return HttpResponse("success")
            else:
                return HttpResponse("分类名称重复")
    else:
        uf = addCategoryForm()
    return render_to_response('category.html', {'uf': uf}, context_instance=RequestContext(request))

def modifyCategory(request):
    if request.method == "POST":
        uf = modifyCategoryForm(request.POST)
        if uf.is_valid():
            name = uf.cleaned_data['name']
            status = uf.cleaned_data['status']
            qcategory = category.objects.filter(name = name)
            if len(qcategory) == 0:
                cate = category()
                cate.name = name
                cate.status = status
                cate.save()
                return HttpResponse("success")
            else:
                return HttpResponse("fail")
    else:
        uf = modifyCategoryForm()
    return render_to_response("modifyCategory.html", {"uf": uf},context_instance=RequestContext(request))


# 商品添加
def addProduct(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            return
    return

