from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from . models import A_class,B_class,G_class
# Create your views here.

def add_c(req):
    list = A_class.objects.all()
    list1 = []
    for var in list:
        dic = {}
        dic['name']   = str(var.name)
        dic['id']   = str(var.id)
        list1.append(dic)



    return render(req,'subadd.html',{'list':list1})
@csrf_exempt
def add_x(req):
    name = req.POST['name']
    desc = req.POST['desc']
    ac_id = req.POST.get('list')
    print('***********')
    print(ac_id)
    print('***********')
    b = B_class()
    b.name = name
    b.desc = desc
    b.ac_id = ac_id
    b.save()
    return HttpResponse('添加成功')