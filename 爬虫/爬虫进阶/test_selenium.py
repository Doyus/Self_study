# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-06 11:30:18
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 12:56:33
from selenium import webdriver
import time
from lxml import etree
driver_path = 'chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')
# print(driver.page_source) #获取源代码


# driver.close():关闭当前页面
# driver.quit(): 退出整个浏览器

# time.sleep(5)
# driver.quit()
#
inputTag = driver.find_element(By.ID,'kw')
inputTag = driver.find_element_by_id('kw')
inputTag = driver.find_element_by_classname('kw')
inputTag = driver.find_element_by_name('kw')
inputTag = driver.find_element_by_xpath('//input[@id="kw"]')
inputTag = driver.find_element_by_css_selector('kw') #通过id获取值
inputTag.send_keys('python') #然后像表单填值

"""
1. 如果只是想要解析网页中的数据，那么推荐将网页源代码扔给lxml来解析，因为lxml底层的使用c语言来写的，所以解析效率会更高

2. 如果想要对元素进行一些个操作，比如给一个文本框输入值，或者是点击某个按钮，那么就必须使用selenium给我们提供的查找元素的方法