#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.template import loader

from models import device
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
            return redirect('/mydevice')

    ctx={}
    ctx.update(csrf(request))
    return HttpResponse("用户名或密码错误")

def homepage(request):
    return render(request, 'monitor/homepage.html')

def device_manage(request):
    if request.user.username != "":
        devicelist = device.objects.all()
        template = loader.get_template('monitor/device_manage.html')
        context = {
            'devicelist':devicelist,
        }
        return HttpResponse(template.render(context,request))

    return render(request, 'monitor/logintips.html')

def my_device(request):
    if request.user.username != "":
        return render(request,'monitor/my_device.html')

    return render(request,'monitor/logintips.html')
def user_logout(request):
    user = request.user
    if user is not None and user.is_active:
        logout(request)
    return redirect('/')

def edit_device(request,name):
    theDevice = device.getdevice(name=name)
    template = loader.get_template('monitor/device_edit.html')
    context = {
        'device': theDevice,
    }
    return HttpResponse(template.render(context, request))