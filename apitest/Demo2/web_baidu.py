# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')

    def test_001(self):
        '''验证百度首页title'''
        self.assertEqual(u'百度一下，你就知道', self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(BaiduTest))
    unittest.TextTestRunner(verbosity=2).run(suite)