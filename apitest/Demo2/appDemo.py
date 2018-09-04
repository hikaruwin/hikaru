# coding: utf-8
from time import sleep
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '4.4.2',
    'appPackage': 'com.taobao.taobao',
    'appActivity': 'com.taobao.tao.welcome.Welcome',
    'automationName': 'Uiautomator2'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 获取屏幕尺寸
size = driver.get_window_size()
print size
# 获取宽带fffffff
print size['width']
# 获取高度
print size['height']
ac = driver.current_activity
print ac
sleep(20)
driver.back()
# 定位toast元素
toast_loc = ("xpath", ".//*[contains(@text, '再按一次返回键退出手机淘宝')]")
t = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
print t