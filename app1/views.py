from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1 import models

# Create your views here.
def index(request):
    if request.method == "GET":
        host_list = models.Hosts.objects.all()
        return render(request, 'index.html', {'host_list': host_list})
    elif request.method == "POST":
        hostname=request.POST.get('hostname')
        ip=request.POST.get('ip')
        platform=request.POST.get('platform')
        description=request.POST.get('des')
        print(hostname,ip,platform,description)
        newobj=models.Hosts(hostname=hostname,ip=ip,platform=platform,description=description)
        newobj.save()
        return redirect('/app1/index/')

def user(request):
    if request.method == "GET":
        user_list = models.Accounts.objects.all()
        group_list = models.Group.objects.all()
        return render(request, 'user.html', {'user_list': user_list,'group_list':group_list})
    elif request.method == "POST":
        username=request.POST.get('name')
        pwd=request.POST.get('pwd')
        role=request.POST.get('role')
        newobj=models.Accounts(username=username,password=pwd,role_id=role)
        newobj.save()
        return redirect('/app1/user/')


def login(request):
    error_msg=''
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd  = request.POST.get('passwd',None)
        obj = models.Accounts.objects.filter(username=user, password=pwd).first()
        if obj != None:
            return redirect('/app1/index/')
        else:
            #用户密码不匹配
            error_msg='用户名或密码错误'
    return render(request,'login.html',{'error_msg':error_msg})

