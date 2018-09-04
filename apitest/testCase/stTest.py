# coding: utf-8

from appium import webdriver
from selenium import webdriver
from page.student import Student
from page.baseTestCase import AppTestCase
import time as t

class studentTest(AppTestCase, Student):
    def testLogin(self):
        t.sleep(5)
        self.login('15812123434', '123456')
        self.driver.get_screenshot_as_file('C:/Users/Administrator/apitest/image/student.png')

if __name__ == '__main__':
    unittest.main(verbosity=2)