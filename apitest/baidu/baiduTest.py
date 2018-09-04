# coding: utf-8

import unittest

from selenium import webdriver

from baidu.Page import baidu


class baiduPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)

    def test_001(self, username=''):
        '''验证用户名为空，点击登录返回的错误信息'''
        baidu.clickLogin(self.driver)
        baidu.typeUsername(self.driver, username)
        baidu.clickButtonLogin(self.driver)
        self.assertEqual(u'请您输入手机/邮箱/用户名', baidu.getErrorText(self.driver))

    def test_002(self, password='admin'):
        '''验证只输入密码，点击登录返回的错误信息'''
        baidu.clickLogin(self.driver)
        baidu.typePassword(self.driver, password)
        baidu.clickButtonLogin(self.driver)
        self.assertEqual(u'请您输入手机/邮箱/用户名', baidu.getErrorText(self.driver))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(baiduPage('test_001'))
    suite.addTest(baiduPage('test_002'))
    unittest.TextTestRunner(verbosity=2).run(suite)