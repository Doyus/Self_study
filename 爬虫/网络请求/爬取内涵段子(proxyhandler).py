# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 11:53:20
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 16:47:48
from urllib import request

url = 'http://httpbin.org/ip'

handler = request.ProxyHandler({
    "http": "123.207.66.220:1080"
    })
opener = request.build_opener(handler)
resp = opener.open(url)
print(resp.read())

"""在代码中使用代理>>
使用urllib.request.ProxyHandler 传入一个代理，这个代理是一个字典，字典的key依赖于代理服务器能够接受的类型，一般是http和https,值是‘IP：port'
使用上一步创建的’opener'.open(url)

使用上一步创建的opener调用open函数发起请求



"""
