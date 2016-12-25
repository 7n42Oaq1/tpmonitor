#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import *

# Create your views here.
from django.template.context_processors import csrf


def index(request):
    return render(request,'monitor/index.html')

def user_login(request):
    if request.POST:
        username = request.POST.get('name')
        password =request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('/homepage')

    ctx={}
    ctx.update(csrf(request))
    return HttpResponse("用户名或密码错误")

def homepage(request):
    return render(request,'monitor/homepage.html')

def device_manage(request):
    return render(request,'monitor/device_manage.html')

def my_device(request):
    return render(request,'monitor/my_device.html')

def logout(request):
    #logout(request)
    return redirect('/')