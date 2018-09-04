# coding: utf-8

import unittest
from selenium import webdriver
from selenium import webdriver

class AppTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = '1d957336'
        desired_caps['appPackage'] = 'com.pnlyy.pnlclass.pnlclass_student'
        desired_caps['appActivity'] = 'com.pnlyy.pnlclass.pnlclass_student.view.StartPageActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()