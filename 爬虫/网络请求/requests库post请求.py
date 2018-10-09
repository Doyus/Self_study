# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 20:15:32
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-04 20:29:23
import requests

data = {
    'first':'true',
    'pn':'1',
    'kd':'php',
}
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'Referer': 'https://www.lagou.com/jobs/list_php?labelWords=&fromSearch=true&suginput=',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400',

}


response = requests.post(url, data=data, headers=headers)
with open('拉勾网测试post-ajax的test.txt','w',encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))
print(response.json())