# coding: utf-8

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import NoSuchElementException
import time as t

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except (NoSuchElementException, KeyError, Exception), e:
            print 'Error details:%s' %(e.args[0])

    @property
    def wait(self):
        t.sleep(5)