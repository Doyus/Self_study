# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-06 15:21:36
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 16:46:21
import requests
from lxml import etree
import time



def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    headers = {
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400',

    }
    data = {
        'first': 'false',
        'pn': 1,
        'kd': 'python'}

    for x in range(1,14):
        data['pn'] = x
        response = requests.post(url,headers=headers, data=data)
        #json的方法，如果饭回来的是json数据，那么这个方法会自动load成字典
        print(response.json())
        time.sleep(1)

request_list_page()

#{'success': False, 'msg': '您操作太频繁,请稍后再访问', 'clientIp': '223.20.133.167'}
#所以导入time.sleep让它休息一秒
