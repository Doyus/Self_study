# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from Spider.items import SpiderItem

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com/']
    start_urls = ['http://qiushibaike.com/text/page/1/']
    base_domain = 'https://www.qiushibaike.com'
    def parse(self, response):
        # contentLeft = response.xpath("//div[@id='content-left']")
        # print("="*30)
        # print(type(contentLeft))
        # print("="*30)
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        for duanzidiv in duanzidivs:
            duanzidiv.xpath('.//h2/text()').get().strip()#可以get可以转化为Unicode字符
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()
            # print(content)
            # duanzi = {"author": author,"content":content}  #由于这个框架不建议直接自己写这个存贮结构，而是建议在items中定义好一个结构，分开使用
            # yield duanzi
            item = SpiderItem(author=author,content=content)
            yield item
        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@fref').get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain+next_url,callback=self.parse)


