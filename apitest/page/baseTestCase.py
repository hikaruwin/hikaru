# coding: utf-8

from appium import webdriver
from selenium import webdriver
import unittest
import os

PATH = lambda p: os.path.join(os.path.dirname(__file__), p)


class AppTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '644d5914'
        # desired_caps['appPackage'] = 'com.pnlyy.pnlclass.pnlclass_student'
        # desired_caps['appActivity'] = 'com.pnlyy.pnlclass.pnlclass_student.view.LoginActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        desired_caps['app'] = PATH('C:\\app-dev-debug8241.apk')
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()
