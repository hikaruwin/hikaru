# coding: utf-8

from appium import webdriver
from selenium import webdriver
from appiumPJ.page.vip import vipLogin
from appiumPJ.page.baseTestCase import AppTestCase
import unittest

class vipTest(AppTestCase, vipLogin):
    def testLogin(self):
        self.login('14155667788', '123456a')
        self.driver.get_screenshot_as_file('C:/Users/Administrator/apitest/appiumPJ/image/vip.png')

if __name__ == '__main__':
    unittest.main(verbosity=2)