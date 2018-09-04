# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

class Baidu(object):
    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        t.sleep(2)

    def clickLogin(self):
        self.wait()
