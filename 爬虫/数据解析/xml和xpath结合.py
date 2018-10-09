# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-05 11:56:51
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 14:33:19
from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tecent.html',parser=parser)

#1. 获取所有tr标签
#//tr
#xpath 返回的是一个列表
trs = html.xpath('//tr')
for tr in trs:
    # print(tr)
    print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))


# 2. 获取第二个tr标签
tr = html.xpath('//tr[2]')[1]  #按照下标进行获取
print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))
#
#3. 获取所有class等于event的标签
tr1 = html.xpath('//tr[@class='event']')
print(etree.tostring(tr1,encoding='utf-8').decode('utf-8'))
#
#4. a 标签中href属性
ab = html.xpath('//a/@href') #这样写可以获取到href的值
for i in ab:
    print(a)

# 5. 获取所有的职位信息(纯文本)
trs = html.xpath('//tr[position()>1]')
for tr in trs:
    href = tr.xpath('.//a')[0]  #这个地方要注意加一个点来表示，当前节点下的a标签，不加点就是取所有的a标签
    fullurl = main_url + href
    title = tr.xpath('.//a/text()')[0]
    title = tr.xpath('.//td[1]//text()')[0]  #这种方式也可以
    category = tr.xpath('./td[2]/text()')[0]
    address = tr.xpath('./td[3]/text()')[0]
    pubtimes = tr.xpath('./td[4]/text()')[0]
    print(title)
    break