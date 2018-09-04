# coding: utf-8

from selenium.webdriver import Remote
from selenium import webdriver

# 启动浏览器驱动
def browser():
    driver = webdriver.Chrome()
    return driver

'''
# 用于测试该脚本是否有效
if __name__ == '__main__':
    dr = browser()
'''
