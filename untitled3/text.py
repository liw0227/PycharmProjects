# coding = utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.title)  # 把页面title 打印出来
driver.find_element_by_name('wd').send_keys('我能做什么')
time.sleep(3)
driver.find_element_by_id('su').click()
