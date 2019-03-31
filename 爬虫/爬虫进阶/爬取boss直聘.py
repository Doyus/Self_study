# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-06 16:48:19
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 17:09:26
import csv
import pytesseract
from urllib import request
from PIL import Image
import re

class BossSpider(object):
    driver_path = 'chromedriver.exe'
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=BossSpider.driver_path)
        pytesseract.pytesseract.tesseract_cmd = r''
        self.url = ''
        self.domain = ''
        fp = open('boss.csv','a',newline='',encoding='utf-8')

        self.writer = csv.DictWriter(fp,['name','company_name',])
        self.writer.writeheader()

    def run(self):
        self.driver.get(self.url)
        while True:
            if len(self.driver_elements_by_id('captcha')) > 0:
                self.fill_captcha()
                time.sleep(2)
                continue
            source = self.driver.page_source
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath