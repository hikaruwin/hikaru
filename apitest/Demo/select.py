# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.maximize_window()
# driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
so = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'kwkw')))
so.send_keys('appium')
driver.quit()