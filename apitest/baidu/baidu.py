# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time as t


def wait():
    t.sleep(2)

def clickLogin(driver):
    wait()
    driver.find_element_by_link_text(u'登录').click()

def typeUsername(driver, username):
    # clickLogin(driver)
    wait()
    driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys(username)

def typePassword(driver, password):
    # clickLogin(driver)
    wait()
    driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys(password)

def clickButtonLogin(driver):
    wait()
    driver.find_element_by_id('TANGRAM__PSP_3__submit').click()

def getErrorText(driver):
    wait()
    return driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_3__error']").text

# 登录方法
def login(driver, username, password):
    clickLogin(driver)
    typeUsername(driver, username)
    typePassword(driver, password)
    clickButtonLogin(driver)

# 获取昵称方法
def getNiCheng(driver):
    wait()
    return driver.find_element_by_xpath(".//*[@id='s_username_top']/span").text

# 退出方法
def exit(driver):
    wait()
    move = driver.find_element_by_xpath(".//*[@id='s_username_top']/span")
    ActionChains(driver).move_to_element(move).perform()
    wait()
    driver.find_element_by_xpath(".//*[@id='s_user_name_menu']/div/a[5]").click()
