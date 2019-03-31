"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url

from myblog import view_fun

urlpatterns = [

    url(r'^g_login$',view_fun.to_login,name='g_log'),
    url(r'^g_regist$',view_fun.regist,name='g_reg'),
    url(r'^g_verify$',view_fun.verify,),
    url(r'^g_add_user$',view_fun.add_user,name='sa'),
    url(r'^g_a$',view_fun.addx,name='xxx'),
    url(r'^g_update$',view_fun.update,name="xiugai"),
    url(r'^g_del$',view_fun.dele),
    url(r'^g_xiugai$',view_fun.xiugai),
    url(r'^ajax$',view_fun.ajax),
    url(r'^toajax$',view_fun.to_ajax),
    url(r'^g_index/$',view_fun.index),
    ]
