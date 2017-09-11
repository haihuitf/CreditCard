#coding:UTF-8
from django.db import models
from django.contrib import admin
import datetime
# Create your models here.


# 用户user
class UserInfo(models.Model):

    id = models.AutoField(primary_key=True,)
    # 用户名
    username = models.CharField(max_length=50, blank=False)
    # 登陆密码
    password = models.CharField(max_length=150, blank=False)
    # 姓名
    name = models.CharField(max_length=1500)
    # 手机号码
    mobile = models.CharField(max_length=150)
    # 是否锁定（0：否，1：是）
    islocked = models.IntegerField(default=0)
    # 绑定卡
    bindcard = models.IntegerField(max_length=150)
    # 账户权限(0:用户,1:管理员)
    role = models.IntegerField(default=0)
    # 是否删除（0：否，1：是）
    isdel = models.IntegerField(default=0)
    # 创建时间
    createTime = models.DateField(auto_now=True)
    # 更新时间
    updateTime = models.DateField(auto_now_add=True)

# 信用卡CardInfo
class CardInfo(models.Model):

    id = models.AutoField(primary_key=True)
    # 用户id
    userId = models.ForeignKey('UserInfo')
    # 卡号
    cardno = models.IntegerField(max_length=150, blank=False)
    # 密码
    password = models.CharField(max_length=150, blank=False)
    # 卡所有者
    owener = models.CharField(max_length=150, blank=False)
    # 卡额度
    credTotla = models.DecimalField(max_digits=19, decimal_places=3)
    # 信用卡透支余额
    creditBalance = models.DecimalField(max_digits=19, decimal_places=3)
    # 信用卡日息
    dayRate = models.FloatField()
    # 提现手续费率
    freeRate = models.FloatField()
    # 是否冻结（0：否,1：是）
    frozenStatus = models.IntegerField(default=0)
    # 创建时间
    createTime = models.DateField(auto_now=True)
    # 更新时间
    updateTime = models.DateField(auto_now_add=True)

#商品product
class product():

    id = models.AutoField(primary_key=True)
    # 分类id
    categoryId = models.ForeignKey("category")
    # 商品编号
    code = models.IntegerField(max_length=150)
    # 商品名称
    productName = models.CharField(max_length=150, blank=False)
    # 商品价格
    price = models.FloatField()
    # 状态（0:否;1:删除）
    status = models.IntegerField(default=0)
    # 库存
    inventory = models.IntegerField()
    # 创建时间
    createTime = models.DateField(auto_now=True)
    # 更新时间
    updateTime = models.DateField(auto_now_add=True)

# 商品分类category
class category():

    id = models.AutoField(primary_key=True)
    # 分类名称
    name = models.CharField(max_length=50, blank=False)
    # 状态（0:否，1：删除）
    status = models.IntegerField(default=0)
    # 创建时间
    createTime = models.DateField(auto_now=True)
    # 更新时间
    updateTime = models.DateField(auto_now_add=True)


