# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-05 14:33:57
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 16:47:41
import requests
from lxml import etree
# 1. 将目标网站的页面抓取下来
url = 'https://movie.douban.com/cinema/nowplaying/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400',
    'Referer':'https://movie.douban.com/',
}
response = requests.get(url,headers=headers)
text = response.text
# text经过解码，content是原生字符串，是str（Unicode）类型字符串，是bytes类型
#

# 2. 将抓取下来的网页进行一定规则提取
# 把内容解码成html
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0] #获取正在上映的电影
# print(etree.tostring(url,encoding='utf-8').decode('utf-8'))

lis = ul.xpath('./li')
movies = []
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title = li.xpath('@data-title')[0] #xpath获取到的都是列表
    score = li.xpath('@data-score')[0]
    duration = li.xpath('@data-duration')[0]
    region = li.xpath('@data-region')[0]
    director = li.xpath('@data-director')[0]
    actors = li.xpath('@data-actors')[0]
    thumbnail = li.xpath('.//img/@src')
    print(title)
    movie = {
        'title': title,
        'score': score,
        'duration': duration,
        'region': region,
        'director': director,
        'actors': actors,
        'thumbnail': thumbnail,
    }
    movies.append(movie)
# print(movies)
