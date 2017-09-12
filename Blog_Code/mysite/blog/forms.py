#coding: utf-8
from django import forms

"""
借此实现博客的评论功能
"""
class CommentForm(forms.Form):
    """
    评论表单用于发表博客的评论。评论表单的类并根据需求定义了三个字段：称呼、邮箱和评论内容。这样我们就能利用它来快速生成表单并验证用户的输入。
    """
    name = forms.CharField(label='称呼',max_length=16,error_messages={
        'required':'请填写您的称呼',
        'max_length':'称呼太长咯'
    })

    email = forms.EmailField(label='邮箱',error_messages={
        'required':'请填写您的邮箱',
        'invalid':'邮箱格式不正确'
    })

    content = forms.CharField(label='评论内容',error_messages={
        'required':'请填写您的评论内容！',
        'max_length':'评论内容太长咯'
    })
#发表博客
class WriteForm(forms.Form):

    title=forms.CharField(label='标题',max_length=32)
    author=forms.CharField(label='作者',max_length=16)
    content=forms.TimeField(label='博客正文')
    #created=forms.DateTimeField(label='发布时间')
#登录表单
class UserForm(forms.Form):
    """
    登录
    """
    username=forms.CharField(label='用户名',max_length=100)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())

