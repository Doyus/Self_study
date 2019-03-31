# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 17:18:48
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-04 20:15:01
import requests

params = {
    'wd': '中国'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400',
}
response = requests.get('https://www.baidu.com/s',params=params, headers=headers)


with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(response.url)

"""笔记
1. response.content:这个是直接从网络上面抓取的数据，没有经过任何的解码。所以是一个bytes类型。

2. response.text: 这个是requests将response.content进行解码的字符串。解码需要指定一个编码方式，requests, 将会根据自己的猜测才判断编码方式，所以有时候会出错，导致解码产生乱码，这时候就应该用response.content.decode('utf-8')

"""

# print(response.text)
# print(type(response.content))
# print(type(response.content.decode('utf-8')))
# 以上两种方式可以获取网页代码，如果产生乱码就解码
#
# print(response.url)
# print(response.encoding)
# print(response.status_code)