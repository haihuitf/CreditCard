from django.shortcuts import render,render_to_response
from CreditCardDjango import settings
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import UserInfo
# Create your views here.



#�û���¼
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #��ȡ���û�����
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #��ȡ�ı����������ݿ���бȽ�
            user = UserInfo.objects.filter(username__exact = username,password__exact = password)
            if user:
                #�Ƚϳɹ�����תindex
                response = HttpResponseRedirect('/online/index/')
                #��usernameд�������cookie,ʧЧʱ��Ϊ3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #�Ƚ�ʧ�ܣ�����login
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})