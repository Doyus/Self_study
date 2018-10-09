# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-08-23 11:35:09
# @Last Modified by:   Marte
# @Last Modified time: 2018-08-28 14:20:42
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import User_info
from . models import Adimn_info
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Count,Min,Max,Sum,Avg
import json
import math

def to_login(req):
    return render(req,'g_login.html')

@csrf_exempt
def verify(request):
    if request.method == 'POST':
        # querySet = User.objects.filter(name=name,pwd=pwd)
        list = User_info.objects.all()
        for var in list:
            if str(var.name) == str(request.POST['name']) and str(var.pwd) == str(request.POST['pwd']):
                req = render(request,'Transfer.html',)
                req.set_cookie('is_log', 'True',max_age=2000)
                req.set_cookie('Name','dong66',max_age=2000)
                req.set_cookie('password','123456',max_age=2000)
                # req.set_cookie('Admin', a,max_age=2000,)
                # req.set_cookie('Password',b,max_age=2000,)
                 # expires=None, path='/', domain=None, secure=None, httponly=False
                return req
            else:
                continue
        return render(request,'g_login.html')

def regist(req):

    return render(req,'g_regist.html')

def add_user(req):
    if req.method == "POST":
        name = req.POST['namea']
        pwd = req.POST['pwd']
        td = User_info()
        td.name = name
        td.pwd  = pwd
        td.save()
        return render(req,'g_login.html') #,locals()  全部把所有参数变为字典传给页面
now_count = 1
def index(req):
    global now_count
    if req.COOKIES.get('is_log'):
        nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        list1 = []
        list = User_info.objects.all()
        # print(list.count())
        total = list.count()
        m_count = total/5
        max_count = math.ceil(m_count)
        # print(max_count)


        p1 = req.GET.get('p')
        print(p1)
        print(type(p1))
        if str(p1)=='x' and now_count < max_count:

            now_count +=1
            print(now_count)
        if str(p1)=='s' and now_count >1:
            now_count =now_count-1

        #
        print(now_count)
        # if p:
        #     now_count +=1
        #     print(now_count)

        for var in list[(now_count-1)*5:(now_count-1)*5+5]:
        # for var in list[0:5]:
            dic = {}
            dic['nameb']   = str(var.name)
            dic['id']   = str(var.id)
            dic['sex'] = str(var.sex)
            dic['age'] = str(var.age)
            dic['pwd']  = str(var.pwd)
            list1.append(dic)
        return render(req,'g_index.html',{'list':list1,'time':nowTime,'total':max_count,'now_count':now_count})
    else:
        return render(req,'g_login.html')
def dele(request):
    idd = request.GET.get('idd')
    User_info.objects.filter(id=idd).delete()
    return render(request,'Transfer.html')
def update(request):
    id1 = request.POST.get('idd')
    name1 = request.POST.get('namex')
    age1 = request.POST.get('agex')
    sex1 = request.POST.get('sexx')
    pwd1 = request.POST.get('pwdx')
    _t = User_info.objects.get(id=id1)
    _t.name=name1
    _t.age=age1
    _t.sex=sex1
    _t.pwd=pwd1
    _t.save()
    return render(request,'Transfer.html')
# @csrf_exempt
def addx(req):
    if req.method == "POST":
        name = req.POST['namex']
        age = req.POST['agex']
        pwd = req.POST['pwdx']
        sex = req.POST['sexx']
        td = User_info()
        td.name = name
        td.age  = age
        td.pwd  = pwd
        td.sex = sex
        td.save()
        return render(req,'Transfer.html') #,locals()  全部把所有参数变为字典传给页面
def to_ajax(req):
    return render(req,'ajax_login.html')
@csrf_exempt
def ajax(request):


    if request.method == 'POST':
        list1 = User_info.objects.all()
        print("**************************")
        b = request.POST['name']
        print(b)
        print(list1)

        print("**************************")
        for var in list1:
            print(var.name)
            if str(var.name) == str(request.POST['name']):
                return HttpResponse('你好！该用户名已注册')
            else:
                return HttpResponse('用户名可以注册')
def xiugai(request):
   id1 = request.GET.get('idd')
   _t = User_info.objects.get(id=id1)
   name1 =_t.name
   age1 = _t.age
   sex1 = _t.sex
   pwd1 = _t.pwd

   return render(request,'g_change.html',{'idb':id1,'nameb':name1,'sexb':sex1,'ageb':age1,'pwdb':pwd1})