# coding: utf-8

import unittest
from case.basetestcase import *
import json
import time

class getVersion(unittest.TestCase):
    verCode2 = ''
    verCode1 = ''
    verCode3 = ''
    uid = ''
    accessUser = ''
    classid1 = '632679'
    recell = '14100000700'
    recell2 = '14100000701'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01(self):
        '''获取验证码（注册）'''
        r = req('login/phone-code', '', '', '0', '192.168.56.1', 'sdsdasd', '2', cellphone=self.recell, type='2', areaCode='+86')
        print r
        self.assertEqual(u'成功', r[u'message'])
        global verCode1
        verCode1 = (r[u'data'])[u'code']
        print verCode1

    def test02(self):
        '''验证验证码（注册）'''
        r = req('login/validate', '', '', '0', '192.168.56.1', 'sdsdasd', '2', cellphone=self.recell, type='2', areaCode='+86', code=str(verCode1))
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test03(self):
        '''用户注册（注册）'''
        r = req('login/register', '', '', '0', '192.168.56.1', 'sdsdasd', '2', username=self.recell, nickName='接口测试', pwd='123456', type='0', areaCode='+86', code=str(verCode1), clientId='7d2a1657cdaa35463daa2e773297248a', channelId='')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test04(self):
        '''用户密码登录'''
        r = req('login/login', '', '', '0', '192.168.56.1', 'sdsdasd', '2', username=self.recell, pwd='123456', type='0', areaCode='+86', clientId='', channelId='', newPwd='123456a')
        print r
        self.assertEqual(u'成功', r[u'message'])
        print r[u'data']
        print type(r[u'data'])
        print (r[u'data'])[u'uid']
        print type((r[u'data'])[u'uid'])
        global uid
        uid = (r['data'])['uid']
        print uid
        print type(uid)
        global accessUser
        accessUser = (r['data'])['accessToken']
        print accessUser

    def test05(self):
        '''用户退出'''
        r = req('user/logout', str(uid), str(accessUser), '0', '192.168.56.1', 'sdsdasd', '2', udid='7d2a1657cdaa35463daa2e773297248a')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test06(self):
        '''获取验证码（登录）'''
        time.sleep(70)
        r = req('login/phone-code', '', '', '0', '192.168.56.1', 'sdsdasd', '2', cellphone=self.recell, type='3', areaCode='+86')
        print r
        self.assertEqual(u'成功', r[u'message'])
        global verCode2
        verCode2 = (r[u'data'])[u'code']
        print verCode2

    def test07(self):
        '''用户验证码登录'''
        r = req('login/login', '', '', '0', '192.168.56.1', 'sdsdasd', '2', username=self.recell, pwd=str(verCode2), type='1', areaCode='+86', clientId='', channelId='', newPwd='123456a')
        print r
        self.assertEqual(u'成功', r[u'message'])
        print r[u'data']
        print type(r[u'data'])
        print (r[u'data'])[u'uid']
        print type((r[u'data'])[u'uid'])
        global uid
        uid = (r['data'])['uid']
        print uid
        print type(uid)
        global accessUser
        accessUser = (r['data'])['accessToken']
        print accessUser

    def test08(self):
        '''获取验证码（忘记密码）'''
        time.sleep(70)
        r = req('login/phone-code', '', '', '0', '192.168.56.1', 'sdsdasd', '2', cellphone=self.recell, type='1', areaCode='+86')
        print r
        self.assertEqual(u'成功', r[u'message'])
        global verCode3
        verCode3 = (r[u'data'])[u'code']
        print verCode3

    def test09(self):
        '''忘记密码'''
        r = req('login/forgot', '', '', '0', '192.168.56.1', 'sdsdasd', '2', cellphone=self.recell, code=str(verCode3), areaCode='+86', pwd='123456a')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # android端，需要提供clientid和channelid
    def test11(self):
        '''获取验证码（注册）'''
        r = req('login/phone-code', '', '', '0', '192.168.56.1', 'sdsdasd', '1', cellphone=self.recell2, type='2', areaCode='+86')
        print r
        self.assertEqual(u'成功', r[u'message'])
        global verCode1
        verCode1 = (r[u'data'])[u'code']
        print verCode1

    def test12(self):
        '''验证验证码（注册）'''
        r = req('login/validate', '', '', '0', '192.168.56.1', 'sdsdasd', '1', cellphone=self.recell2, type='2', areaCode='+86', code=str(verCode1))
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test13(self):
        '''用户注册（注册）'''
        r = req('login/register', '', '', '0', '192.168.56.1', 'sdsdasd', '1', username=self.recell2, nickName='接口测试', pwd='123456a', type='0', areaCode='+86', code=str(verCode1), clientId='7d2a1657cdaa35463daa2e773297248a', channelId='6')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test14(self):
        '''用户密码登录'''
        r = req('login/login', '', '', '0', '192.168.56.1', 'sdsdasd', '1', username=self.recell2, pwd='123456', type='0', areaCode='+86', clientId='7d2a1657cdaa35463daa2e773297248a', channelId='6', newPwd='123456a')
        print r
        self.assertEqual(u'成功', r[u'message'])
        print r[u'data']
        print type(r[u'data'])
        print (r[u'data'])[u'uid']
        print type((r[u'data'])[u'uid'])
        global uid
        uid = (r['data'])['uid']
        print uid
        print type(uid)
        global accessUser
        accessUser = (r['data'])['accessToken']
        print accessUser

    def test15(self):
        '''用户退出'''
        r = req('user/logout', str(uid), str(accessUser), '0', '192.168.56.1', 'sdsdasd', '1', udid='7d2a1657cdaa35463daa2e773297248a')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test16(self):
        '''获取验证码（登录）'''
        time.sleep(70)
        r = req('login/phone-code', '', '', '0', '192.168.56.1', 'sdsdasd', '1', cellphone=self.recell2, type='3', areaCode='+86')
        print r
        self.assertEqual(u'成功', r[u'message'])
        global verCode2
        verCode2 = (r[u'data'])[u'code']
        print verCode2

    def test17(self):
        '''用户验证码登录'''
        r = req('login/login', '', '', '0', '192.168.56.1', 'sdsdasd', '1', username=self.recell2, pwd=str(verCode2), type='1', areaCode='+86', clientId='7d2a1657cdaa35463daa2e773297248a', channelId='6', newPwd='123456a')
        print r
        self.assertEqual(u'成功', r[u'message'])
        print r[u'data']
        print type(r[u'data'])
        print (r[u'data'])[u'uid']
        print type((r[u'data'])[u'uid'])
        global uid
        uid = (r['data'])['uid']
        print uid
        print type(uid)
        global accessUser
        accessUser = (r['data'])['accessToken']
        print accessUser

    def test18(self):
        '''获取验证码（忘记密码）'''
        time.sleep(70)
        r = req('login/phone-code', '', '', '0', '192.168.56.1', 'sdsdasd', '1', cellphone=self.recell2, type='1', areaCode='+86')
        print r
        self.assertEqual(u'成功', r[u'message'])
        global verCode3
        verCode3 = (r[u'data'])[u'code']
        print verCode3

    def test19(self):
        '''忘记密码'''
        r = req('login/forgot', '', '', '0', '192.168.56.1', 'sdsdasd', '1', cellphone=self.recell2, code=str(verCode3), areaCode='+86', pwd='123456a')
        print r
        self.assertEqual(u'成功', r[u'message'])

if __name__ == '__main__':
    unittest.main(verbosity=2)