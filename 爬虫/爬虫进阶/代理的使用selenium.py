# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-06 14:54:03
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 14:58:19
from selenium import webdriver

driver_path = 'chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server-http://58.48.168.166:51430")
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)

driver.get('http://httpbin.org/ip')