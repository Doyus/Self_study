# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-06 15:00:41
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 15:20:39
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

submitBtn = driver.find_element_by_id('su')

print(type(submitBtn))#class 'selenium.webdriver.remote.webelement.WebElement'>
print(submitBtn.get_attribute('value'))
print(submitBtn.is_selected('value'))
print(submitBtn.is_enabled('value'))
print(submitBtn.find_element_by_id('value'))
print(submitBtn.find_elements_by_id('value'))
driver.save_screenshot('baidu.png')

