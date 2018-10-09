# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 03:04:59
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-04 03:11:11
from urllib import parse

url = 'http://www.baidu.com/s?wd=python'

result = parse.urlparse(url)

print(result)

print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('query:',result.query)
print('fragment:',result.fragment)


# urlsplit它是分割
#
# urlsplit里面params没有，其他和urlparse差不多