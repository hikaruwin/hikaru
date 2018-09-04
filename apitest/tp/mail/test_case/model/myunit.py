# coding: utf-8

from time import sleep
import unittest
from .driver import browser
from .function import insert_img

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.url = 'http://mail.163.com'
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
