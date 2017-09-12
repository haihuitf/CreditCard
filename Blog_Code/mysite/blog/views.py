#coding: utf-8
from django.shortcuts import render,render_to_response



# Create your views here.
from django.db.models import *
from models import *
from forms import CommentForm,UserForm,WriteForm
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger,InvalidPage


def get_blogs(request):
    #获取所有的文章
    page_size=2
    blogs = Blog.objects.all().order_by('-created')
    paginator = Paginator(blogs,page_size)
    page=request.GET.get('page')
    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    except EmptyPage:
        blogs=paginator.page(paginator.num_pages)
    return render_to_response('blog_list.html',{'blogs':blogs},context_instance=RequestContext(request))

#详情页
def get_details(request,blog_id):
    #comments=Comment.objects.all()
    try:
        #文章的内容
        blog = Blog.objects.get(id=blog_id)
        #评价数
        ls=Blog.objects.all()
        for i in range(1,len(ls)+1):
            comment_count=Comment.objects.filter(blog_id=i).count()
            cont_count=Blog.objects.filter(id=i).update(content_count=comment_count)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-created'),
        'form':form,
    }
    return render(request,'blog_details.html',ctx)

#编辑
def get_write(request,blog_id):
    try: blog=Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:raise Http404
    if request.method=='GET':
        form=WriteForm()
    else:
        form=WriteForm(request.POST)
        if form.is_valid():
            cleaned_data= form.cleaned_data
            cleaned_data['blog']=blog
            #created=form.cleaned_data['created']
            Blog.objects.create(**cleaned_data)
    ctx={
        'blog':blog,
        'writes':blog.comment_set.all(),
        'form':form
    }
    return render_to_response(request,'blog_write.html')

#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))


#登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/blogs/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))
#登陆成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

def test(request):
    return render(request,'test.html')
