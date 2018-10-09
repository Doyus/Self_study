# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-06 11:30:18
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 13:10:48
from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.support.ui import Select
driver_path = 'chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')
# print(driver.page_source) #获取源代码

inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')

time.sleep(3)
inputTag.clear()  #清楚表单中内容

# *****************操作checkbox*******
#
rememberBtn = driver.find_element_by_name('jumpMenu')
rememberBtn.click()

# *****************操作select*******
from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.support.ui import Select
driver.get('http://www.doban.cn/')

selectBtn = Select(driver.find_element_by_name('jumpMenu'))
selectBtn.select_by_index(1)
selectBtn.select_by_value('95秀客户端')