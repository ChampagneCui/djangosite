from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1 import models


# Create your views here.
def index(request):
	if request.method == "GET":
		host_list = models.Hosts.objects.all()
		hgroup_list = models.HGroup.objects.all()
		return render(request, 'index.html', {'host_list': host_list,'hgroup_list': hgroup_list})
	elif request.method == "POST":
		if request.POST.get('func') == 'add':
			hostname = request.POST.get('hostname')
			hgroup_id = request.POST.get('hgroup_id')
			ip = request.POST.get('ip')
			platform = request.POST.get('platform')
			description = request.POST.get('des')
			print(hostname, ip, platform, description)
			newobj = models.Hosts(hostname=hostname,group_id=hgroup_id,ip=ip, platform=platform, description=description)
			newobj.save()
		elif request.POST.get('func') == 'del':
			id = request.POST.get('id')
			models.Hosts.objects.filter(id=id).delete()
		elif request.POST.get('func') == 'update':
			id = request.POST.get('id')
			hostname = request.POST.get('hostname')
			hgroup_id = request.POST.get('hgroup_id')
			ip = request.POST.get('ip')
			platform = request.POST.get('platform')
			description = request.POST.get('des')
			newobj=models.Hosts.objects.filter(id=id)
			newobj.update(hostname=hostname)
			newobj.update(group_id = hgroup_id)
			newobj.update(ip=ip)
			newobj.update(platform=platform)
			newobj.update(description=description)
		return redirect('/app1/index/')


def user(request):
	if request.method == "GET":
		user_list = models.Accounts.objects.all()
		group_list = models.Group.objects.all()
		return render(request, 'user.html', {'user_list': user_list, 'group_list': group_list})
	elif request.method == "POST":
		if request.POST.get('func') == 'add':
			username = request.POST.get('name')
			pwd = request.POST.get('pwd')
			role = request.POST.get('role')
			newobj = models.Accounts(username=username, password=pwd, role_id=role)
			newobj.save()
		elif request.POST.get('func') == 'del':
			id = request.POST.get('id')
			models.Accounts.objects.filter(id=id).delete()
		elif request.POST.get('func') == 'update':
			id = request.POST.get('id')
			pwd = request.POST.get('pwd')
			role = request.POST.get('role')
			newobj = models.Accounts.objects.filter(id=id)
			if pwd != '':
				newobj.update(password=pwd)
			newobj.update(role_id=role)
		return redirect('/app1/user/')


def login(request):
	error_msg = ''
	if request.method == "POST":
		user = request.POST.get('user', None)
		pwd = request.POST.get('passwd', None)
		obj = models.Accounts.objects.filter(username=user, password=pwd).first()
		if obj != None:
			return redirect('/app1/index/')
		else:
			# 用户密码不匹配
			error_msg = '用户名或密码错误'
	return render(request, 'login.html', {'error_msg': error_msg})
