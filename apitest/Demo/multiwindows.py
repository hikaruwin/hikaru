# coding: utf-8

from selenium import webdriver
import time as t

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.maximize_window()
t.sleep(3)
driver.find_element_by_partial_link_text(u'登录').click()
t.sleep(5)
# 获取当前窗口的句柄
nowHandle = driver.current_window_handle
driver.find_element_by_css_selector(".pass-reglink").click()
t.sleep(3)
# 获取所有窗口的句柄
handles = driver.window_handles
for handle in handles:
    if handle != nowHandle:
        driver.switch_to_window(handle)
        print u'我跳转到了注册页面'
        t.sleep(3)
        driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys('123456789')
        t.sleep(5)
        driver.close()
driver.switch_to_window(nowHandle)
print u'我回到了登录页面'
t.sleep(3)
driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys('123456789')
t.sleep(5)
driver.quit()