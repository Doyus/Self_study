# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 17:09:30
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-04 17:17:32
from urllib import request
from http.cookiejar import MozillaCookieJar

# cookiejar = MozillaCookieJar('cookie.txt')
# cookiejar.load(ignore_discard=True)# 从外部加载cookie
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)

# resp = opener.open('http://www.baidu.com/')

# cookiejar.save()

# ---------------------------------------------------
cookiejar = MozillaCookieJar('cookies.txt')
cookiejar.load(ignore_discard=True)# 从外部加载cookie
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://www.baidu.com/')
for cookie in cookiejar:
    print(cookie)