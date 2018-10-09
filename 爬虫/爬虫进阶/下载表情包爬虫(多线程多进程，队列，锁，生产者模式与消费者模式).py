# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-05 21:17:15
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 09:42:16
import requests
from lxml import etree
from urllib import request
import os
import re
def parse_page(url):
    headers = {
        'Referer': 'http://www.doutula.com/photo/list/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
    for img in imgs:
        # print(etree.tostring(img))
        # data-original="https://ws2.sinaimg.cn/bmiddle/9150e4e5ly1fvnsqcsftoj20u01hc0ym.jpg"
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r'[\?？\.。！!]',"",alt)
        suffix = os.path.splitext(img_url)[1] #os的这个模块可以分割后缀名与名字，是一个元组形式
        filename = alt + suffix

        request.urlretrieve(img_url,'imgs/'+filename)
        # print(filename)
        # print(img_url)



def main():
    for x in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d' %x
        parse_page(url)
if __name__ == "__main__":
    main()





