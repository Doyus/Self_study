# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

# class SpiderPipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json",'w',encoding='utf-8')

#     def open_spider(self, spider): #爬虫打开来以后就会调用这个函数
#         print('爬虫开始了')

#     def process_item(self, item, spider):#如果爬虫过程中你传了一些数据回来，就会调用这个函数
#         # item_json = json.dumps(item,ensure_ascii=False)
#         item_json = json.dumps(dict(item),ensure_ascii=False) #如果用了items那个来进行数据结构，那么就应该用dict转化为字典
#         self.fp.write(item_json+'\n')
#         return item

#     def close_spider(self, spider):#爬虫结束会调用这个函数
#         self.fp.close()
#         print('爬虫结束了')


'''另一种方式下载'''
from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter
class SpiderPipeline(object):
    def __init__(self):
        self.fp = open("duanzi.json",'wb')
        self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        self.exporter.start_exporting()

    def open_spider(self, spider): #爬虫打开来以后就会调用这个函数
        print('爬虫开始了')

    def process_item(self, item, spider):

        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):#爬虫结束会调用这个函数\
        self.exporter.finish_exporting()
        self.fp.close()
        print('爬虫结束了')

# JsonItemExporter方式得到结果是：先把所有结果放到内存中，等到self.exporter.finish_exporting()时把它同一加到一个列表，这样的话，如果数据量非常大，会占用大量内存，因此引出了另一个模块
# '''另一种方式下载'''
# from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter
# class SpiderPipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json",'wb')
#         self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()

#     def open_spider(self, spider): #爬虫打开来以后就会调用这个函数
#         print('爬虫开始了')

#     def process_item(self, item, spider):

#         self.exporter.export_item(item)
#         return item

#     def close_spider(self, spider):#爬虫结束会调用这个函数\
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print('爬虫结束了')
