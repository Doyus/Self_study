# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 16:22:48
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-04 17:08:19
from urllib import request
from urllib import parse
from http.cookiejar import cookieJar
# 1. 登陆
# 1.1 创建一个cookiejar对象
cookiejar = cookieJar()
# 1.2 使用cookiejar创建一个opener
opener = request.build_opener(handler)
# 1.3 使用上一步创建的handler创建一个opener
header = {
    'User-Agent':"",
}
data = {
    'email':'34434432@qq.com',
    'password':'pythonspider',
}
login_url = 'http://www.renren.com/PLogin.do'
req = request.Request(login_url,data-parse.urlencode(data).encode('utf-8'),headers=headers)
opener.open(req)

#访问主页
dong_url = ''
# 获取个人主页的页面的时候，不要新建一个opener
# 而应该使用之前的那个opener，因为之前opener已经包含了登陆所需要的信息
req = request.Request(dong_url,headers=header)
resp = opener.open(req)
with open('reren.html','wb',encoding='utf-8') as fp:
    fp.write(resp.read().decode('uft-8'))