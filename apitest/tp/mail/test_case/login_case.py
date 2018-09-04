# coding: utf-8

from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.login_page import LoginPage
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):
    def test_login_user_pwd_null(self):
        '''用户名密码为空登录'''
        po = LoginPage(self.driver, self.url, u'网易')
        po.open()
        po.login_action('', '')
        sleep(2)
        self.assertEqual(po.login_error_hint(), u'请输入帐号')
        function.insert_img(self.driver, 'user_pwd_null.png')