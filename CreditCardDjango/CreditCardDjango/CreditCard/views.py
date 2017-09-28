#coding:UTF-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import UserInfo, CardInfo, category, product
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import datetime
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
                            return HttpResponseRedirect('/productList/')
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

# 退出登陆
@login_required
def logout(request):
    response = HttpResponse("logout!!!")
    response.delete_cookie('username')
    return response

# 编辑用户信息
# @login_required表示登录状态才会调用此模块

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
            if len(qcategory) != 0:
                category.objects.filter(name = name).update(name = name,
                                                            status = status,
                                                            )
                return HttpResponse("success")
            else:
                return HttpResponse("fail")
    else:
        uf = modifyCategoryForm()
    return render_to_response("modifyCategory.html", {"uf": uf},context_instance=RequestContext(request))


# 商品添加
def addProduct(request):
    if request.method == "POST":
        uf = addProductForm(request.POST)

        print(type)
        if uf.is_valid():
            productName = uf.cleaned_data['productName']
            price = uf.cleaned_data['price']
            inventory = uf.cleaned_data['inventory']
            code = 123
            # 保存数据库
            addP = product()
            addP.productName = productName
            addP.inventory = inventory
            addP.price = price
            addP.code = code
            addP.save()
            return HttpResponse("success")
        else:
            return  HttpResponse("fail")
    else:
        uf = addProductForm()
    return render_to_response("addProduct.html", {"uf":uf}, context_instance=RequestContext(request))

# 商品修改
def modifyProduct(request):
    if request.method == "POST":
        uf = modifyProductForm(request.POST)
        if uf.is_valid():
            productName = uf.cleaned_data["productName"]
            status = uf.cleaned_data["status"]
            price = uf.cleaned_data['price']
            inventory = uf.cleaned_data['inventory']
            modifyproduct = product.objects.filter(productName = productName)
            if len(modifyproduct) != 0:
                product.objects.filter(productName = productName).update(productName = productName,
                                                                         price = price,
                                                                         inventory = inventory,
                                                                         status = status,
                                                                         code = 123)
                return HttpResponse("success")
            else:
                return HttpResponse("modify fail")
        else:
            return HttpResponse("fail")
    else:
        uf = modifyProductForm()
    return render_to_response("modifyProduct.html", {"uf":uf}, context_instance=RequestContext(request))

# 商品列表
def productList(request):
    productlist = product.objects.all()
    return render_to_response('productList.html',{'productlist':productlist},context_instance=RequestContext(request))

# 订单列表
def saleOrder(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            productList = uf.cleaned_data['productList']
            cost = uf.cleaned_data['cost']

    return

def ProductDetails(request):
    IdNumber=['C']
    if request.method == "POST":
        print("insert")
        if 'Create' in request.POST:#新建商品
            print('gouer')
            if ProductDetail.objects.filter(ProdcutID=request.POST['ProductID']):
                return HttpResponse('success')
                # return HttpResponseRedirect('ProductList/%s' % str(request.POST['ProductID']+'C'))
            else:
                NewProduct = ProductDetailForm(request.POST)
                if NewProduct.is_valid():
                    SaveNew = NewProduct.save(commit=False)
                    SaveNew.ProductID = request.POST['ProductID'][0:4]
                    SaveNew.save()
                    return HttpResponseRedirect('/ProductList/%s' % str(request.POST['ProductID'][0:4]+"E"))
                # 修改商品
        elif 'Modify' in request.POST:
            ProductDetail.objects.filter(ProdcutID=request.POST['ProductID'][0:4]).update(
                ProductName=request.POST['ProductName'],
                ProductPrice=request.POST['ProductPrice'],
                ProductNumber=request.POST['ProductNumber'],
                ProductOffer=request.POST['ProductOffer']
            )
            return HttpResponse('Modify')
        # 加入购物车
        elif 'AddCar' in request.POST:
            InputCar = MyCars.objects.create(ProdcutID=request.POST['ProductID'][0:4],
                                             ProductName=request.POST['ProductName'],
                                             ProductPrice=request.POST['ProductPrice'])
            InputCar.save()
            return HttpResponse('AddCar')
            #return HttpResponseRedirect('')
        # 立即购买
        elif 'BuyNow' in request.POST:
            request.session['ProductID'] = request.POST['ProductID'][0:4]
            request.session['ProductName'] = request.POST['ProductName']
            request.sessioHttpResponsen['ProductPrice'] = request.POST['ProductPrice']
            return ('BuyNow')
            #return HttpResponseRedirect('')
        # 我的购物车
        else:
            return HttpResponse('MyCar')
            #return HttpResponseRedirect('')
    else:
        if IdNumber[-1] == 'C':
            types = '已存在'
        elif IdNumber[-1] == 'z':
            types = '已新增'
        elif IdNumber[-1] == 'A':
            types = '已加入购物车'
        elif IdNumber[-1] == 'M':
            types = '已修改'
        else:
            types = ''
        #fromValue = ProductDetail.objects.filter(ProductID=IdNumber[0:4])[0]
        fromValue = ProductDetailForm(())
        return render_to_response('ProductDetail.html', {'form': fromValue, 'types': types}, context_instance=RequestContext(request))







