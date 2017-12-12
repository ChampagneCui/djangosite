from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    error_msg=''
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd  = request.POST.get('passwd',None)
        if user == 'root' and pwd == '123':
            return render(request,'home.html')
        else:
            #用户密码不匹配
            error_msg='用户名或密码错误'
    return render(request,'login.html',{'error_msg':error_msg})
