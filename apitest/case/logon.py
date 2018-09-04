# coding: utf-8

import unittest
from case.basetestcase import *
import json


class getVersion(unittest.TestCase):
    verCode2 = ''
    verCode1 = ''
    verCode3 = ''
    uid = ''
    accessUser = ''
    classid1 = '46449'
    recell='14100010004'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01(self):
        '''获取验证码（注册）'''
        r = req('https://api-dev.pnlyy.com/v4/login/phone-code', '', '', '2.2.0', '0', '192.168.56.1', 'sdsdasd', '1', cellphone=self.recell, type='2', areaCode='+86')
        print r
        self.assertEqual(u'成功', r[u'message'])
        global verCode1
        verCode1 = (r[u'data'])[u'code']
        print verCode1

    def test02(self):
        '''用户注册（注册）'''
        r = req('https://api-dev.pnlyy.com/v4/login/register', '', '', '2.1.0', '0', '192.168.56.1', 'sdsdasd', '1', username=self.recell, nickName='app_测试闫金泉', pwd='123456a', type='0', areaCode='+86', code=str(verCode1))
        print r
        self.assertEqual(u'成功', r[u'message'])