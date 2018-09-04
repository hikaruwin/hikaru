# coding: utf-8

import unittest
from case.basetestcase import *

class getVersion(unittest.TestCase):
    verCode2 = '12345'
    uid = ''
    accessUser = ''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01(self):
        '''获取验证码'''
        r = req('https://api-dev.pnlyy.com/v4/login/phone-code', '', '', '2.1.0', '0', '192.168.56.1', 'sdsdasd', '1', cellphone='15100000788', type='2', areaCode='+86')
        print r
        print type(r)
        self.assertEqual(u'成功', r[u'message'])

    # def test02(self):
    #     '''获取版本信息'''
    #     r = req('https://api-dev.pnlyy.com/v4/login/version', '', '', '2.0.2', '1', '192.168.56.1', 'sdsdasd', '1', clientType='1')
    #     print r
    #     print type(r)
    #     self.assertEqual(u'成功', r[u'message'])

    # def test03(self):
    #     '''获取验证码'''
    #     r = req('https://api-dev.pnlyy.com/v4/login/phone-code', '', '', '2.0.4', '0', '192.168.56.1', 'sdsdasd', '1', cellphone='14100000001', type='2', areaCode='+86')
    #     print r
    #     print type(r)
    #     self.assertEqual(u'成功', r[u'message'])

    # def test04(self):
    #     '''获取验证码'''
    #     r = req('https://api4.pnlyy.com/v4/login/phone-code', '', '', '2.0.4', '0', '192.168.56.1', 'sdsdasd', '1', cellphone='18400000100', type='2', areaCode='+86')
    #     print r
    #     print type(r)
    #     self.assertEqual(u'成功', r[u'message'])