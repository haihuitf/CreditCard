#coding: utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    """
    博客分类
    """
    name = models.CharField('名称',max_length=30)
    created_time=models.DateTimeField('创建时间',auto_now_add=True)
    last_modify_time=models.DateTimeField('修改时间',auto_now_add=True)


    def __unicode__(self):
        return self.name

class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField('名称',max_length=16)
    created_time=models.DateTimeField('创建时间',auto_now_add=True)
    last_modify_time=models.DateTimeField('修改时间',auto_now_add=True)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者',max_length=16)
    content = models.TextField('博客正文')
    created = models.DateTimeField('发布时间',auto_now_add=True)
    category = models.ForeignKey(Category,verbose_name='分类')
    tags = models.ManyToManyField(Tag,verbose_name='标签')
    content_count=models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog,verbose_name='博客')
    name = models.CharField('称呼',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length=240)
    created = models.DateTimeField('发布时间',auto_now_add=True)
    content_count=models.IntegerField(default=0)


    def __unicode__(self):
        return self.content

class User(models.Model):
    """
    用户登录
    """
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __unicode__(self):

        return self.username

