#coding:UTF-8
from django import forms



#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


class RegistForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    name = forms.CharField(label="姓名")
    mobile = forms.CharField(label="手机号码")
    bindcard = forms.CharField(label="信用卡号")