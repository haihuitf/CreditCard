from django.shortcuts import render
from CreditCardDjango.CreditCardDjango import settings
# Create your views here.


#��
class UserForm(forms.Form):
    username = forms.CharField(label='�û���',max_length=100)
    password = forms.CharField(label='����',widget=forms.PasswordInput())

#�û���¼
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #��ȡ���û�����
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #��ȡ�ı����������ݿ���бȽ�
            user = User.objects.filter(username__exact = username,password__exact = password)
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
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req)