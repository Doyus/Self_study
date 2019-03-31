# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-04 21:04:25
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 11:56:13
from lxml import etree
'''笔记：
1. 解析html字符串： 使用lxml.etree.HTML进行解析

2. 解析HTML文件：使用lxml.etree.parse进行操作，这个函数默认使用的是xml解析器，代码有时候会碰到一些不规范的HTML,这时候就会解析错误，这时候就要自己创建HTML解析器
'''
# text = """
# <div>
#     <ul>
#         <li class="item-0"><a href="#">first——item</a></li>
#         <li class="item-1"><a href="#">second--item</a></li>
#         <li class="item-inactive"><a href="#">third--item</a></li>
#         <li class="item-1"><a href="#">fourth--item</a></li>
#         <li class="item-0"><a href="#">fifth--item</a>  #注意此处缺少一个</li>闭合标签
#     </ul>
# </div>
# """
# # 利用etree.HTML 将字符串转化为html文档
# html = etree.HTML(text)

# # 按字符串序列化HTML文档
# result = etree.tostring(html)

# print(result)

'''从文件中读取html代码'''

# 读取外部文件 baidu.html
html = etree.parse('baidu.html')
result = etree.tostring(html,encoding='utf-8')
print(result.decode('utf-8'))