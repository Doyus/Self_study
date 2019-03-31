# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 11:13:15
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 16:47:51
from urllib import request
from urllib import parse
# url = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='

#ajax的url
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

data = {
    'first':'true',
    'pn':'1',
    'kd':'python'
}
# resp = request.urlopen(url)
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400',
    'Host':'www.lagou.com',
    'Origin':'https://www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
}

req = request.Request(url,headers=header,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(req)

print(resp.read().decode('utf-8'))


# TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str,如果没有写.encode('utf-8')，因为python3默认是Unicode字符串
#
#
# b'{"success":false,"msg":"\xe6\x82\xa8\xe6\x93\x8d\xe4\xbd\x9c\xe5\xa4\xaa\xe9\xa2\x91\xe7\xb9\x81,\xe8\xaf\xb7\xe7\xa8\x8d\xe5\x90\x8e\xe5\x86\x8d\xe8\xae\xbf\xe9\x97\xae","clientIp":"223.20.133.167"}\n'然后又报这个错误，因为b开头,所以加了.decode('utf-8')查看，然后会显示{"success":false,"msg":"您操作太频繁,请稍后再访问","clientIp":"223.------------其实并没有操作太频繁，浏览器还是能访问，这就说明网站识别了你的爬虫程序，需要使得你的请求头更加真实；处理方式是又在请求头中加入了Host:www.lagou.com
# Origin:https://www.lagou.com
# Referer:https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=