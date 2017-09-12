#coding:UTF-8
from django import forms



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

# 商品分类
class Category(forms.Form):
    name = forms.CharField(label="分类名称", max_length=100)

class ChangePwdForm(forms.Form):
    username = forms.CharField(label="用户名")
    old_password = forms.CharField(label="原密码",widget=forms.PasswordInput())
    new_password = forms.CharField(label="新密码",widget=forms.PasswordInput())