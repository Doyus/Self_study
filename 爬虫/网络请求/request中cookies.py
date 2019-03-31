# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 20:46:46
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-04 21:03:30
import requests

# response = requests.get('https://www.baidu.com/')
# print(response.cookies)

# print(response.cookies.get_dict())
#
url = ''

data = {
    'email': '234244234@qq.com',
    'password': 'pythonspider',
}
headers = {
    'User-Agent': '',
}

session = requests.Session()
session.post(url,data=data,headers=headers)

response.post(url, data=data,headers=headers)

response = session.get('http://www.baidu.com')

with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.text)

'''笔记
如果post方式返回的是json数据，那么可以调用response.json()来将json字符串为字典或者列表。
###使用代理
在请求方式中传递proxies参数就可以了
###处理cookies：
如果想要在多次请求中共享cookie，那么应该使用session
####处理不被信任的ssl证书：
解决：resp = requests.get(url,verify=False)
'''
