# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 基本层
class Base(object):
    def __init__(self, driver, base_url, pagetitle):
        self.driver = driver
        self.base_url = base_url
        self.pagetitle = pagetitle
        self.timeout = 30

    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    def _open(self, url, pagetitle):
        self.driver.maximize_window()
        self.driver.get(url)
        sleep(2)
        assert self.on_page(pagetitle), u"打开开页面失败 %s" % url

    def open(self):
        self._open(self.base_url, self.pagetitle)

    # *参数个数不是固定
    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print u"%s 页面中未能找到 %s 元素" % (self, loc)


    def iframe(self, iframeid):
        return self.driver.switch_to.frame(iframeid)

    def iframe_out(self):
        return self.driver.switch_to.default_content()
