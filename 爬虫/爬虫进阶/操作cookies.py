from selenium import webdriver
import time
from lxml import etree
driver_path = 'chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')

for cookie in driver.get_cookies():
    print(cookie)

print("*"*30)

print(driver.get_cookies('PSTM'))

driver.delete_all_cookies()