# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-06 14:40:56
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 14:52:55
from selenium import webdriver

driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

driver.execute_script("window.open('https://douban.com/')")
driver.execute_script("window.open('https://doutula.com/')")
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])
print(driver.current_url)
'''
1. 虽然在窗口中切换到了新的页面，但是driver中还没有切换
2. 如果想要在代码中切换到新的页面，并且做一些爬虫那么就应该使用driver.switch_to_window来切换到指定窗口
3. driver.window.handler是一个列表，里面装的都是窗口句柄他会按照窗口打开的顺序