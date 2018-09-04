# coding: utf-8

from selenium import webdriver
import sys
from time import sleep
from threading import Thread

reload(sys)
sys.setdefaultencoding('utf-8')

def baidu_search(browser, url):
    driver = None
    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    if driver == None:
        exit()
    print u'开始【case_0001】百度搜索'
    driver.get(url)
    print u'清除搜索中数据，输入搜索关键词'
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys('selenium')
    print u'单击百度一下按钮开始搜索'
    driver.find_element_by_id('su').click()
    sleep(5)
    print u'关闭浏览器，退出webdriver'
    driver.quit()

if __name__ == '__main__':
    data = {
        'ie': 'http://www.baidu.com',
        'firefox': 'http://www.baidu.com',
        'chrome': 'http://www.baidu.com'
    }
    threads = []
    for b, url in data.items():
        t = Thread(target=baidu_search, args=(b, url))
        threads.append(t)
    for thr in threads:
        thr.start()