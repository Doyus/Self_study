from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time
global headers
headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive'}

driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://finance.ifeng.com/shanklist/1-66-')

time.sleep(5)  # 留出加载时间

links = driver.find_elements_by_xpath("//*[@id='root']/div[5]/div[1]/div/ul/li/div/h2/a")  # 获取到所有a标签，组成一个列表
length = len(links)  # 列表的长度，一共有多少个a标签

for i in range(0, length):  # 遍历列表的循环，使程序可以逐一点击
    links = driver.find_elements_by_xpath("//*[@id='root']/div[5]/div[1]/div/ul/li/div/h2/a")  # 在每次循环内都重新获取a标签，组成列表
    link = links[i]  # 逐一将列表里的a标签赋给link
    url = link.get_attribute('href')  # 提取a标签内的链接，注意这里提取出来的链接是字符串
    driver.get(url)  # 不能用click，因为click点击字符串没用，直接用浏览器打开网址即可
    time.sleep(1)  # 留出加载时间
    title = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[1]/div[1]/h1").text  # .text的意思是指输出这里的纯文本内容
    print(title)
    driver.back()  # 后退，返回原始页面目录页
    time.sleep(3)  # 留出加载时间

print(length)

