#coding:UTF-8
from django import forms
from .models import *



#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

#注册
class RegistForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    name = forms.CharField(label="姓名")
    mobile = forms.CharField(label="手机号码")
    bindcard = forms.CharField(label="信用卡号")

# 修改密码
class ChangePwdForm(forms.Form):
    username = forms.CharField(label="用户名")
    old_password = forms.CharField(label="原密码",widget=forms.PasswordInput())
    new_password = forms.CharField(label="新密码",widget=forms.PasswordInput())

# 商品分类
class addCategoryForm(forms.Form):
    name = forms.CharField(label="分类名称", max_length=100)

# 修改商品分类
class modifyCategoryForm(forms.Form):
    name = forms.CharField(label="分类名称", max_length=100)
    status = forms.ChoiceField(label="分类状态", choices=[('0', '0'), ('1', '1')])

# 添加商品
class addProductForm(forms.Form):
    productName = forms.CharField(label="商品名称",max_length=100)
    price = forms.CharField(label="商品价格",max_length=100)
    inventory = forms.CharField(label="商品库存",max_length=100)

# 修改商品
class modifyProductForm(forms.Form):
    productName = forms.CharField(label="商品名称",max_length=100)
    price = forms.CharField(label="商品价格",max_length=100)
    inventory = forms.CharField(label="商品库存",max_length=100)
    status = forms.ChoiceField(label="商品状态", choices=[('0', '0'), ('1', '1')])

class ProductDetailForm(forms.Form):
    ProductID = forms.CharField(label="商品名称",max_length=100)
    ProductName = forms.CharField(label="商品名称",max_length=100)
    ProductPrice = forms.CharField(label="商品价格",max_length=100)
    ProductNumber = forms.CharField(label="商品库存",max_length=100)
    ProductOffer = forms.CharField(label="商品库存",max_length=100)
