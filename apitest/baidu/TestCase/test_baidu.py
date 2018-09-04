# coding: utf-8

# import unittest
#
# from ddt import ddt, data, unpack
# from selenium import webdriver
# from baidu.Page import basetestcase
# from baidu.Page import baidu
# from baidu.model import Model
# from baidu.model.Model import DataHelper
#
#
# # @ddt
# class baiduPage(basetestcase.BaseTestCase, Model.DataHelper):
#
#     # def testLoginFail_001(self):
#     #     '''验证:用户名密码为空，点击登录返回的提示信息'''
#     #     baidu.login(self.driver, BasePage.readCsv(0, 0), BasePage.readCsv(0, 1))
#     #     self.assertEqual(BasePage.readCsv(0, 2), baidu.getErrorText(self.driver))
#     #
#     # def testLoginFail_002(self):
#     #     '''验证:只输入用户名，点击登录返回的提示信息'''
#     #     baidu.login(self.driver, BasePage.readCsv(1, 0), BasePage.readCsv(1, 1))
#     #     self.assertEqual(BasePage.readCsv(1, 2), baidu.getErrorText(self.driver))
#     #
#     # def testLoginFail_003(self):
#     #     '''验证:输入错误的用户名和密码，点击登录返回的提示信息'''
#     #     baidu.login(self.driver, BasePage.readCsv(2, 0), BasePage.readCsv(2, 1))
#     #     self.assertEqual(BasePage.readCsv(2, 2), baidu.getErrorText(self.driver))
#
#     # @data(*DataHelper.readExcels())
#     # @unpack
#     def testFailLogin(self):
#         baidu.login(self.driver, self.readExcel(1, 0), self.readExcel(1, 1))
#         self.assertEqual(self.readExcel(1, 2), baidu.getErrorText(self.driver))

import unittest
from baidu.Page.basetestcase import BaseTestCase
from baidu.Page.baidu import BaiduPage
from baidu.Page.homePage import HomePage
from baidu.model import Model
from ddt import ddt, data, unpack

@ddt
class baiduPage(BaseTestCase, BaiduPage, HomePage):
    @data(*Model.DataHelper().readExcel())
    @unpack
    def testLogin_001(self, username, password, context_expxcted):
        '''测试百度登录失败的N种情况'''
        self.doLogin(username, password)
        self.assertEqual(context_expxcted, self.getLoginErrorDiv())

    def testLogin_002(self):
        '''测试百度登录成功的情况'''
        db = Model.DataHelper()
        self.login(db.getXmlUser('login', 'niCheng'), self.getNiCheng())



if __name__ == '__main__':
    unittest.main(verbosity=2)

