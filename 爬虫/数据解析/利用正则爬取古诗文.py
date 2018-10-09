# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-05 19:29:21
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 20:21:09
import requests
import re
def parse_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'
    }
    response = requests.get(url,headers)
    text = response.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)

    #此处因注意 . 号不能匹配/n ,但是取值要用到，因此加了DOTALL来匹配所有
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)

    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)
    print(content_tags)
    print('88888888888888888888888888888')
    contents = []
    for content in content_tags:
        # print(content)
        x = re.sub(r'<.*?>',"",content)
        contents.append(x.strip())
    poems = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        poem = {
            'title':title,
            'dynasty':dynasty,
            'author':authors,
            'content':content,
        }
        poems.append(poem)
    for poem in poems:
        print(poem)
        print('*'*30)
def main():
    url = 'https://www.gushiwen.org/default_1.aspx'
    parse_page(url)

if __name__ == '__main__':
    main()
# url = 'https://www.gushiwen.org/default_1.aspx'
# parse_page(url)

# 因为贪婪模式所以只打印了一最后一个结果,所以需要在.* 改变为.*? 非贪婪模式