# coding: utf-8

import unittest
from case.basetestcase import *
import json


class getVersion(unittest.TestCase):
    verCode2 = ''
    verCode1 = ''
    # global uid, accessUser
    uid = '97895'
    accessUser = '1801010212136bfae093c91d1431b391b76ce05186b8c339b08fba0529d42a82a87efe061ec'
    classid1 = '160143'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01(self):
        '''用户登录账号'''
        r = req('login/login', '', '', '0', '192.168.56.1', 'sdsdasd', '1', username='18010102121', pwd='123456', type='0', areaCode='+86', clientId='7d2a1657cdaa35463daa2e773297248a', channelId='5')
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

    def test02(self):
        '''等级列表页'''
        r = req('achievement/level-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test03(self):
        '''勋章列表页'''
        r = req('achievement/medal-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test04(self):
        '''勋章弹出层'''
        r = req('achievement/medal-dialog', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test05(self):
        '''勋章弹出通知'''
        r = req('achievement/medal-notice', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', medalId='["AABB","BBCC","CCDD"]')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test06(self):
        '''学生成长统计'''
        r = req('achievement/statistics', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', type='1')
        print r
        self.assertEqual(u'成功', r[u'message'])


    # def test07(self):
    #     '''学生成长统计'''
    #     r = req('activity/red-point-count', str(uid), str(accessUser), '0',
    #             '192.168.56.1', 'sdsdasd', '1')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])