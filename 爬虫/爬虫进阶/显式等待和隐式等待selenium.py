'''
现在的网页越来越多的采用了Ajax技术，这样程序便不能确定何时向某个元素完全加载出来了，如果实际页面等待时间过长导致某个dom元素还没出来，但是你的代码直接使用了这个webElement，那么就会抛出NullPointer异常，为了解决这个问题，所以selenium 提供了两种等待方式，一种隐式等待，一种是显示等待
1. 隐式的等待：
    调用driver.implicitly_wait。那么在获取不可用的元素之前，会先等待十秒钟的时间
2. 显式等待：
    显式等待是表明某个条件成立后才执行获取元素的操作，也可以等待的时候指定一个最大的时间，如果超过这个时间，那么就抛出一个异常，显示等待应该用selenium.webdriver.support.excepted_conditions
    和selenium.webdriver.support.ui.WebDriveWait来配合完成
3. 一些其他条件的等待：
    1）presence_of_element_located:某个元素已经加载完毕了。
    2）presence_of_all_emement_located:网页中所有满足条件的元素都加载完了
    3）element_to_cliable: 某个元素是可以点击。
'''
# from selenium import webdriver

# driver_path = r'chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)

# driver.get('https://www.douban.com/')

# driver.implicitly_wait(20)

# driver.find_element_by_id('adfjalsd')
#以上的意思是：
#   去请求一个不存在的id，如果没有隐式的等待，就会直接报错，加上就会等待指定时间后抛出异常
'''指定条件触发'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver_path = r'chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com/')

# driver.implicitly_wait(20)

WebDriverWait(driver,10).until(
    EC.presence_of_element_located(By.ID,'sfaf')
)