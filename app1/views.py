from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
list=[{'hostname':'HostA','ip':'1.1.1.1','description':'test_server'}]


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
        if user == 'root' and pwd == '123':
            return redirect('/app1')
        else:
            #用户密码不匹配
            error_msg='用户名或密码错误'
    return render(request,'login.html',{'error_msg':error_msg})
