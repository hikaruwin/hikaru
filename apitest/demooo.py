# coding: utf-8

from appium import webdriver
import time

desired_caps = {
    'platformName': 'Android',
    'deviceName': '192.168.113.101:5555',
    'platformVersion': '4.4.4',
    'appPackage': 'com.pnlyy.pnlclass_teacher',
    'appActivity': 'com.pnlyy.pnlclass_teacher.view.StartPageActivity'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_id('com.pnlyy.pnlclass_teacher:id/etUserName').send_keys(u'13112233446')
time.sleep(2)
driver.find_element_by_id('com.pnlyy.pnlclass_teacher:id/etPassword').send_keys('123456')
time.sleep(2)
driver.find_element_by_name(u'登录').click()
time.sleep(5)
driver.find_element_by_name(u'个人中心').click()
time.sleep(2)
driver.find_element_by_name(u'修改密码').click()
time.sleep(2)
driver.find_element_by_id('com.pnlyy.pnlclass_teacher:id/passwordEt').send_keys('123456')
driver.find_element_by_id('com.pnlyy.pnlclass_teacher:id/newPassWord').send_keys('123456a')
driver.find_element_by_id('com.pnlyy.pnlclass_teacher:id/repeatPassWord').send_keys('123456a')
driver.find_element_by_name(u'确认').click()
driver.quit()