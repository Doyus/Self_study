# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 02:48:50
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 16:47:58
from urllib import request
from urllib import parse

# params = {'name':'张三','age':18, 'greet':'hello world'}

# result = parse.urlencode(params)

url = 'https://www.baidu.com/s?'

params = {'wd':'刘德华'}
qs = parse.urlencode(params)
url = url + '?' + qs

resp = request.urlopen(url)

print(url)
print(parse.parse_qs(url))