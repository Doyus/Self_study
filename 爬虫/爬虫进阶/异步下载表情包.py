# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-05 21:17:15
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 10:44:26
import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading

class Procuder(threading.Thread):

    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Procuder,self).__init__(*args,**kwargs)
        self.page_queue = page_queue#页面url队列，多个
        self.img_queue = img_queue#图片url队列，多个

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)
    def parse_page(self,url):
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
            alt = re.sub(r'[\?？\.。！!\*]',"",alt)
            suffix = os.path.splitext(img_url)[1] #os的这个模块可以分割后缀名与名字，是一个元组形式
            filename = alt + suffix
            self.img_queue.put((img_url,filename))
            # request.urlretrieve(img_url,'imgs/'+filename)
            # print(filename)
            # print(img_url)

class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:

            if self.img_queue.empty() and self.page_queue.empty():

                break
            img_url, filename = self.img_queue.get()
            request.urlretrieve(img_url,'imgs/'+filename)
            print(filename+'下载完成')



def main():
    page_queue = Queue(100)#存贮多个页面
    img_queue = Queue(1000)#储存多个图片
    for x in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d' %x
        page_queue.put(url)

    for x in range(5):
        t = Procuder(page_queue,img_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == "__main__":
    main()





