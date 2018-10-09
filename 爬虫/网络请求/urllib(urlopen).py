# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 02:36:29
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 22:13:22
from urllib import request

resp = request.urlopen('http://www.baidu.com')
print(resp.read(10))
print(resp.readline())
print(resp.getcode())



# urlopen 默认是get，加上data参数weipost
