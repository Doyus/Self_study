# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 20:42:46
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-04 20:46:10
import requests

proxy = {
    'http': '117.90.6.140:9000',
}

response = requests.get('http://httpbin.org/ip', proxies=proxy)

print(response.text)