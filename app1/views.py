from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1 import models

# Create your views here.
list=[{'hostname':'HostA','ip':'1.1.1.1','description':'test_server','platform':'linux'}]

def index(request,user):
    if request.method == "POST":
        hostname=request.POST.get('hostname')
        ip=request.POST.get('ip')
        platform=request.POST.get('platform')
        description=request.POST.get('des')
        temp={'hostname':hostname,'ip':ip,'description':description,'platform':platform}
        list.append(temp)
    return render(request,'index.html',{'host_list':list,"user":user})

def home(request):
    if request.method == "POST":
        hostname=request.POST.get('hostname')
        ip=request.POST.get('ip')
        description=request.POST.get('des')
        temp={'hostname':hostname,'ip':ip,'description':description}
        list.append(temp)
    return render(request,'home.html',{'host_list':list})

def login(request):
    error_msg=''
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd  = request.POST.get('passwd',None)
        obj = models.Accounts.objects.filter(username=user, password=pwd).first()
        if obj != None:
            return redirect('/app1/index/',{'user':user})
        else:
            #用户密码不匹配
            error_msg='用户名或密码错误'
    return render(request,'login.html',{'error_msg':error_msg})

