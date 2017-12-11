from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    return HttpResponse('Hello')

def login(requests):
    if requests.method == "POST":
        user = requests.POST.get('user',None)
        pwd  = requests.POST.get('passwd',None)
        if user == 'root' and pwd == '123':
            return credits('www.baidu.com')
        else:
            #用户密码不匹配

    else:
        return render(requests,'login.html')