# coding: utf-8

import unittest
from case.basetestcase import *
import json


class getVersion(unittest.TestCase):
    verCode2 = ''
    verCode1 = ''
    uid = ''
    accessUser = ''
    classid1 = '24575791'


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01(self):
        '''获取版本信息'''
        r = req('login/version', '', '', '0', '192.168.56.1', 'sdsdasd', '1',
                clientType='1')
        # clientType手机系统 0ios 1android 2iphone老师
        print r
        print type(r)
        self.assertEqual(u'成功', r[u'message'])

    def test02(self):
        '''用户登录账号'''
        r = req('login/login', '', '', '0', '192.168.56.1', 'sdsdasd', '1',
                username='14155667788', pwd='123456a', type='0', areaCode='+86',
                clientId='7d2a1657cdaa35463daa2e773297248a', channelId='5', newPwd='123456a')
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

    # def test03(self):
    #     '''获取验证码'''
    #     r = req('https://api-dev.pnlyy.com/v4/login/phone-code', '', '', '2.1.0', '0', '192.168.56.1', 'sdsdasd', '1', cellphone='15812123434', type='2', areaCode='+86')
    #     print r
    #     global varCode1
    #     self.assertEqual(u'成功', r[u'message'])
    #     verCode1 = (r[u'data'])[u'code']
    #     print verCode1
    #
    # def test04(self):
    #     '''忘记密码获取验证码'''
    #     r = req('https://api-dev.pnlyy.com/v4/login/phone-code', '', '', '2.1.0', '0', '192.168.56.1', 'sdsdasd', '1',
    #             cellphone='14155667788', type='1', areaCode='+86')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #     global verCode2
    #     verCode2 = (r[u'data'])[u'code']
    #     print verCode2
    #
    # def test05(self):
    #     '''忘记密码'''
    #     r = req('https://api-dev.pnlyy.com/v4/login/forgot', '', '', '2.1.0', '0', '192.168.56.1', 'sdsdasd', '1',
    #             cellphone='14155667788', pwd='123456a', code='verCode1', areaCode='+86')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test06(self):
        '''获取用户信息'''
        r = req('user/get-user-info', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', channelId='7d2a1657cdaa35463daa2e773297248a', clientId='5')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test07(self):
        '''用户退出'''
        r = req('user/logout', self.uid, self.accessUser, '0', '192.168.56.1',
                'sdsdasd', '1', udid='7d2a1657cdaa35463daa2e773297248a')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test08(self):
        '''判断用户是否已登录'''
        r = req('user/is-login', self.uid, self.accessUser, '0', '192.168.56.1',
                'sdsdasd', '1', udid='7d2a1657cdaa35463daa2e773297248a')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test09(self):
        '''个人中心用户详情'''
        r = req('user/get-user-contents', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test10(self):
        '''个人中心修改密码'''
        r = req('user/update-password', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', oldPwd='123456a', newPwd='123456a')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test11(self):
        '''个人中心投诉建议'''
        r = req('user/feedback', self.uid, self.accessUser, '0', '192.168.56.1',
                'sdsdasd', '1', content='极大似乎打算')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test12(self):
        '''乐谱库乐谱列表'''
        r = req('book/book-list', self.uid, self.accessUser, '0', '192.168.56.1',
                'sdsdasd', '1', keyword='哥', categoryId='1', page='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test13(self):
        '''乐谱库曲目'''
        r = req('book/catalog', self.uid, self.accessUser, '0', '192.168.56.1',
                'sdsdasd', '1', keyword='哥', bookId='1', page='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test14(self):
        '''乐谱库曲谱'''
        r = req('book/song-info', self.uid, self.accessUser, '0', '192.168.56.1',
                'sdsdasd', '1', songId='5')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test15(self):
    #     '''首页获取老师课程列表'''
    #     r = req('https://api-dev.pnlyy.com/v4/home/teacher-home', str(uid), str(accessUser), '2.1.0', '0', '192.168.56.1', 'sdsdasd', '1',  day='5')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test16(self):
        '''学生首页课信息'''
        r = req('home/student-home', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', page='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test17(self):
    #     '''首页获取老师课详情，需要crm那边操作开课获得classId'''
    #     r = req('https://api-dev.pnlyy.com/v4/home/teacher-detail', str(uid), str(accessUser), '2.0.2', '0', '192.168.56.1', 'sdsdasd', '1', classId='936551')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test18(self):
        '''首页获取学生课详情'''
        r = req('home/student-detail', self.uid, self.accessUser, '0', '192.168.56.1', 'sdsdasd', '1',
                classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test19(self):
        '''获取课程进度，需要crm那边操作开课获得classId'''
        r = req('course/get-class-schedule', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test20(self):
        '''获取上课乐谱信息，需要crm那边操作开课获得classId'''
        r = req('course/get-image', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test21(self):
        '''添加自主上传信息'''
        r = req('class-image/add-auto', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, name='07-24 17:52:33',
                filePath='[{"rotate":0,"url":"www.baidu.com"},{"rotate":0,"url":"www.baidu.com"}]', showName=u'咏唱调')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test22(self):
        '''添加/删除课乐谱，需要crm那边操作开课获得classId'''
        r = req('class-image/class-song', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, songId='1901', type='0', songIdStr='1901')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test23(self):
        '''获取自主上传的图片信息，需要crm那边操作开课获得classId，并获得自主上传的name'''
        r = req('class-image/auto-info', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, name='07-24 17:52:33')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test24(self):
        '''编辑课自主上传图片，需要crm那边操作开课获得classId，并有自主上传图片的name'''
        r = req('class-image/update-auto', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, name='07-24 17:52:33',
                filePath='[{"rotate":0,"url":"http://pic.baike.soso.com/ugc/baikepic2/0/ori-20170531213657-819831287.jpg/800"}]', showName=u'咏唱调')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test25(self):
        '''获取学生近期的乐谱信息'''
        r = req('class-image/nearest', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', studentId='1275')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test26(self):
    #     '''获取学生的最新的课后单'''
    #     r = req('https://api-dev.pnlyy.com/v4/record/near-record', str(uid), str(accessUser), '2.1.0', '0', '192.168.56.1', 'sdsdasd', '1', studentId='347')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    # def test27(self):
    #     '''老师退出教室的理由'''
    #     r = req('https://api-dev.pnlyy.com/v4/course/out-class', str(uid), str(accessUser), '2.0.2', '0', '192.168.56.1', 'sdsdasd', '1', )
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    def test28(self):
        '''呼叫对方'''
        r = req('push/call-dev', self.uid, self.accessUser, '0', '192.168.56.1',
                'sdsdasd', '1', content='打算大厦将颠', params='229550', title='上课了', type='1', otherUid='889')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test29(self):
        '''保存会议室信息'''
        r = req('course/save-room', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, roomId='1000', roomUrl='www.baidu.com')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test30(self):
        '''保存上课记录信息'''
        r = req('course/class-schedule', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, classStarted='1503306000', nowSongId='',
                nowSongName='ceshi')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test31(self):
    #     '''老师获取学生的历史课后单'''
    #     r = req('https://api-dev.pnlyy.com/v4/record/student-list', '1637', '182905689853f41d92e0de585fc130dc4b6534c055f', '2.0.2', '1', '192.168.56.1', 'sdsdasd', '1', studentId='1275', page='1')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    def test32(self):
        '''获取课后单列表'''
        r = req('record/list', self.uid, self.accessUser, '0', '192.168.56.1',
                'sdsdasd', '1', recordStatus='2', page='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test33(self):
        '''编辑和添加课后单详情'''
        r = req('record/record-detail', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test34(self):
    #     '''学生读取老师评价过的课后单（废弃）'''
    #     r = req('https://api-dev.pnlyy.com/v4/record/student-read', str(uid), str(accessUser), '2.2.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', recordId='2069')
    #     print r
    #     self.assertEqual(u'没有查到数据', r[u'message'])

    def test35(self):
        '''记录sdk调用日志'''
        r = req('netease/log-error', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, code='200', userName='15812123434',
                nickName='测试学生18', reason='缺少xx', classStart='1500008989', classEnd='1500009898', type='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test36(self):
        '''记录课程相关日志信息'''
        r = req('log/class-log', self.uid, self.accessUser, '0', '192.168.56.1',
                'sdsdasd', '1', classId=self.classid1, type='3')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test37(self):
        '''保存上课中的网络状态'''
        r = req('course/class-net', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, line='1', netDesc='1', userName='15812123434')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test38(self):
        '''提交调用接口日志信息'''
        r = req('service/set-log', self.uid, self.accessUser, '0', '192.168.56.1',
                'sdsdasd', '1', content='["student,https://api4.pnlyy.com/v3/student/get-user"]')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test39(self):
        '''修改用户头像'''
        r = req('user/upload-avatar', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', headName='user/head_icon/20170817115323.jpg')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test40(self):
        '''用户修改设备信息'''
        r = req('user/update-user-device', self.uid, self.accessUser, '0', '192.168.56.1', 'sdsdasd', '1',
                clientID='', clientType='0', deviceInfor='ios9.0', versionType='2',
                udid='7d2a1657cdaa35463daa2e773297248a')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test41(self):
        '''删除课自主上传图片和添加最近自主上传'''
        r = req('class-image/auto-operate', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, name='07-24 17:52:33', type='0', oldClassId='2')
        print r
        self.assertEqual(u'目标文件不存在', r[u'message'])

    def test42(self):
        '''获取七牛的token'''
        r = req('tripartite/get-qiniu-token', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', type='6')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test43(self):
        '''学生添加录音，需要classid和七牛key'''
        r = req('course/save-audio', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1,
                audio='reord/audio/cf95cddf810323f4922494816970e877')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test44(self):
        '''保存上课录音，需要classid和七牛key'''
        r = req('course/save-channel', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1,
                channelId='reord/audio/cf95cddf810323f4922494816970e877')
        print r
        self.assertEqual(u'成功', r[u'message'])

    #
    # def test45(self):
    #     '''保存和提交课后单,需要classid'''
    #     r = req('https://api-dev.pnlyy.com/v4/record/add-record', str(uid), str(accessUser), '2.0.2', '0', '192.168.56.1', 'sdsdasd', classId='933071', coherence='', noteAccuracy='', performance='', rhythmAccuracy='', totalScore='', process='', selfAudio='', audio='', image='', type='0')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    # def test46(self):
    #     '''保存和提交课后单'''
    #     r = req('https://api-dev.pnlyy.com/v4/record/add-record', str(uid), str(accessUser), '2.1.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', classId='14030', coherence='', noteAccuracy='', performance='', rhythmAccuracy='', totalScore='', process='', selfAudio='', aduioTime='', audio='', image='', type='0')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test47(self):
        '''获取分类'''
        kw = {}
        r = req('user/category-list', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', **kw)
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test48(self):
    #     '''用户注册'''
    #     r = req('https://api-dev.pnlyy.com/v4/login/register', '', '', '2.0.2', '0',
    #             '192.168.56.1', 'sdsdasd', '1', username='12345678911', areaCode='+86', nickName='doudou', pwd='123456', type='0', code='1', channelId='', clientId='')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    def test49(self):
        '''获取国家的区号'''
        kw = {}
        r = req('login/country-code', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', **kw)
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test50(self):
    #     '''验证验证码'''
    #     r = req('https://api-dev.pnlyy.com/v4/login/validate', str(uid), str(accessUser), '2.0.2', '0',
    #             '192.168.56.1', 'sdsdasd', '1', cellphone='15812123434', areaCode='1', type='1', code='1')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test51(self):
        '''捕获用户的信息'''
        r = req('user/add-user-info', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', sex='1', categoryId='1', age='10', learnTime='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test52(self):
        '''发送消息'''
        r = req('message/send-message', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', uuid='50bd300c-4e6f-6fdc-9157-f3bd4e1935b3', messageType='1', text='10',
                imagePath='', voicePath='')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test53(self):
        '''获取历史消息'''
        r = req('message/history-list', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', uuid='298fbcc7-445f-ff08-57fe-2d6e19cbe55a', is_chat='1', offset='0',
                limit='20')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test54(self):
        '''获取表情包列表'''
        r = req('message/get-face-list', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test55(self):
        '''获取用户的uuid'''
        r = req('message/get-user-uuid', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', clientAppId='105a9656a17b58b552433')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test56(self):
        '''客户端关闭聊天链接'''
        r = req('message/link-close-con', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', client_id='MTkyLjE2OC40MC4yMjBfOTUwNV8xMDM0Nw==')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test57(self):
    #     '''运营活动配置'''
    #     kw = {}
    #     r = req('https://api-dev.pnlyy.com/v4/activity/config', str(uid), str(accessUser), '2.1.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', **kw)
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test58(self):
        '''学生获取课程要求详情'''
        r = req('course/get-class-mark', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test59(self):
        '''学生保存课程备注'''
        r = req('course/class-remark', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, remarkOut='aabb',
                remarkOutImage='["www.a.imag","www.a.imag"]', type='0')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test60(self):
        '''学生关闭、开启同步接口'''
        r = req('user/sync-music', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', type='1')
        print r
        self.assertEqual(u'用户已关闭自动同步乐谱功能', r[u'message'])

    def test61(self):
        '''用户自动同步乐谱是否开启'''
        r = req('user/is-sync-open', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test62(self):
    #     '''课程线路小开关'''
    #     r = req('https://api-dev.pnlyy.com/v4/course/class-line', str(uid), str(accessUser), '2.1.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, justalkOpen='1', yunxinOpen='1')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    # def test63(self):
    #     '''编辑课后单(老师),需要classid'''
    #     r = req('https://api-dev.pnlyy.com/v4/record/update-record', str(uid), str(accessUser), '2.1.0', '0',
    #             '192.168.56.1', 'sdsdasd', recordId='933071', coherence='', noteAccuracy='', performance='',
    #             rhythmAccuracy='', totalScore='', process='', selfAudio='', audio='', image='')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    # def test64(self):
    #     '''获取课后单详情'''
    #     r = req('https://api-dev.pnlyy.com/v4/record/record-info', '347', '1415566778875a853715251748a104fd65542efbabf', '2.1.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', classId='')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test65(self):
        '''获取网络信息'''
        r = req('netease/add-network', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, context=u'云信很好')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test66(self):
        '''运营活动弹窗记录'''
        r = req('activity/dialog-count', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', activityNo='VIP20171102199010', type='1')
        print r
        self.assertEqual(u'运营活动不存在', r[u'message'])

    def test67(self):
        '''获取点赞列表'''
        r = req('open-api/laud-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test68(self):
        '''提交学生对老师评价'''
        r = req('record/add-assess', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', recordId='8263', tagIds='[1,2,3,4]', comment=u'122暗示但是多', grade='1')
        print r
        self.assertEqual(u'此课程，您无权对老师进行评价', r[u'message'])

    def test69(self):
        '''点赞统计'''
        r = req('log/add-laud', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', classId='2069', laudId='1')
        print r
        self.assertEqual(u'此课程，您无权对学生进行点赞操作', r[u'message'])

    def test70(self):
        '''app获取h5界面失败日志记录'''
        r = req('log/err-html', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', postUrl='http://baidu.com', postData='[{"key":"value"}]',
                returnData='[{"key":"value"}]')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test71(self):
        '''app的系统其它日志'''
        r = req('log/monitor', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', type='1', userTime='1513835476')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test72(self):
    #     '''等级列表页'''
    #     r = req('https://api-dev.pnlyy.com/v4/achievement/level-list', str(uid), str(accessUser), '2.2.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', )
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    # def test73(self):
    #     '''勋章列表页'''
    #     r = req('https://api-dev.pnlyy.com/v4/achievement/medal-list', str(uid), str(accessUser), '2.2.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', )
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    # def test74(self):
    #     '''勋章列表页'''
    #     r = req('https://api-dev.pnlyy.com/v4/achievement/week-star', str(uid), str(accessUser), '2.1.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', )
    #     print r
    #     self.assertEqual(u'请求地址异常', r[u'message'])

    # def test75(self):
    #     '''勋章弹出层'''
    #     r = req('https://api-dev.pnlyy.com/v4/achievement/medal-dialog', str(uid), str(accessUser), '2.2.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', )
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    # def test76(self):
    #     '''勋章弹出通知'''
    #     r = req('https://api-dev.pnlyy.com/v4/achievement/medal-notice', str(uid), str(accessUser), '2.2.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', medalId='["AABB","BBCC","CCDD"]')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    # def test77(self):
    #     '''首次课程的弹出信息'''
    #     r = req('https://api-dev.pnlyy.com/v4/log/first-comment', str(uid), str(accessUser), '2.2.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, loveTeacher='0', loveWho='0', holeTeacher='0')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    # def test78(self):
    #     '''学生成长统计'''
    #     r = req('https://api-dev.pnlyy.com/v4/achievement/statistics', str(uid), str(accessUser), '2.2.0', '0',
    #             '192.168.56.1', 'sdsdasd', '1', type='1')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test79(self):
        '''问题调查结果的弹出提交'''
        r = req('log/class-comment-open', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1)
        print r
        self.assertEqual(u'查询课程错误，请确认后在操作', r[u'message'])

    def test80(self):
        '''问题调查结果信息提交'''
        r = req('log/first-comment', '97133',
                '141556677882f355c0882d39c0aefb402d96d558017', '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, loveTeacher='0', loveWho='0', holeTeacher='0')
        print r
        self.assertEqual(u'查询课程错误，请确认后在操作', r[u'message'])

    def test81(self):
        '''验证密码'''
        r = req('user/pwd-verification', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', password='123456a')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test82(self):
        '''内购课程'''
        r = req('user/class-purchase', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test83(self):
        '''用户再次同步云信'''
        r = req('user/synchro-yun', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test84(self):
        '''新版乐谱库历史搜索关键字列表'''
        r = req('book/search-history-keyword', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', instrumentId='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test85(self):
        '''新版乐谱库热门搜索关键字列表'''
        r = req('book/search-hot-keyword', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', instrumentId='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test86(self):
        '''新版乐谱库列表'''
        r = req('book/lately-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', instrumentId='1', page='1', pageSize='3')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test87(self):
        '''新版乐谱库搜索列表'''
        r = req('book/search-lately-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', instrumentId='1', keyword=u'上海')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test88(self):
        '''新版乐谱库乐谱名列表'''
        r = req('book/course-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', bookId='1', isDesc='1', page='1', pageSize='3')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test89(self):
        '''新版乐谱库自主上传列表'''
        r = req('book/private-course-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, instrumentId='1', isDesc='1', page='1', pageSize='3')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test90(self):
        '''新版乐谱库自主上传乐谱图片'''
        r = req('book/private-course-image', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, name='04-09 20:45:05')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test91(self):
        '''新版乐谱库搜索乐谱名列表'''
        r = req('book/search-course-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', bookId='1', instrumentId='1', page='1', pageSize='3', keyword=u'上海')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test92(self):
        '''新版乐谱库乐谱图片'''
        r = req('book/course-image', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', courseId='1601')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test93(self):
        '''新学生首页'''
        r = req('home/student-home-new', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', appTime='1523462400')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test94(self):
        '''手动同步上节课乐谱'''
        r = req('course/sync-music', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, instrumentId='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test95(self):
        '''新学生首页付费用户获取7天课程日历'''
        r = req('home/get-student-class-table', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', day='1', appTime='1523462400')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test96(self):
        '''新学生首页获取用户30天课程'''
        r = req('home/get-student-class-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', page='1', appTime='1523462400', pageSize='3')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test97(self):
        '''手动同步上节课课程要求'''
        r = req('course/sync-class-mark', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, instrumentId='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test98(self):
        '''新版批量自主上传接口'''
        r = req('class-image/batch-auto-operate', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, list='[{"name":"07-3113:17:02","oldClassId":"47837483"},{"name":"07-3113:17:02","oldClassId":"47837484"},{"name":"07-3113:17:02","oldClassId":"47837485"}]')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test99(self):
        '''学生课后单内操作'''
        r = req('record/leave', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', recordId='1', type='1', pageToken='2')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test100(self):
        '''课后单分享'''
        r = req('push/share', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', recordId='1', shareMode='1', shareType='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test101(self):
        '''游客聊天模式下的未读消息'''
        r = req('message/tourist-red-point', '', '', '0',
                '192.168.56.1', 'sdsdasd', '1', uuid='de2aba21-df85-9b88-35d0-90155d23c788')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test102(self):
    #     '''学分首页接口'''
    #     r = req('credit/index', str(uid), str(accessUser), '0',
    #             '192.168.56.1', 'sdsdasd', '1', )
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    # def test103(self):
    #     '''学分兑换记录接口'''
    #     r = req('credit/record-exchange', str(uid), str(accessUser), '0',
    #             '192.168.56.1', 'sdsdasd', '1', )
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    # def test104(self):
    #     '''学分获取接口'''
    #     r = req('credit/get_credit', str(uid), str(accessUser), '0',
    #             '192.168.56.1', 'sdsdasd', '1', credit='11', title=u'55分钟钢琴陪练课')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    # def test105(self):
    #     '''学分的获取、消耗记录接口'''
    #     r = req('credit/credit-record', str(uid), str(accessUser), '0',
    #             '192.168.56.1', 'sdsdasd', '1', type='1')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    # def test106(self):
    #     '''商品详情接口'''
    #     r = req('credit/goods-details', str(uid), str(accessUser), '0',
    #             '192.168.56.1', 'sdsdasd', '1', goodId='1', type='1')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    # def test107(self):
    #     '''确认兑换接口'''
    #     r = req('credit/confirmation-exchange', str(uid), str(accessUser), '0',
    #             '192.168.56.1', 'sdsdasd', '1', goodId='1', type='1', credit='11', account=str(uid), password='123456a', num='1')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    # def test108(self):
    #     '''兑换结果页面'''
    #     r = req('credit/exchange-result', str(uid), str(accessUser), '0',
    #             '192.168.56.1', 'sdsdasd', '1', orderId='1', type='1', goods_id='8')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    # def test109(self):
    #     '''获取QQ头像和昵称'''
    #     r = req('credit/get-user-qq-info', str(uid), str(accessUser), '0',
    #             '192.168.56.1', 'sdsdasd', '1', account='814360749')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])
    #
    # def test110(self):
    #     '''获取QQ头像和昵称'''
    #     r = req('notice/user-unread-notice-list', str(uid), str(accessUser), '0',
    #             '192.168.56.1', 'sdsdasd', '1', )
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test111(self):
        '''课程取消展示页'''
        r = req('course/cancel-class', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test112(self):
        '''课程取消确认接口'''
        r = req('course/do-class-cancel', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test113(self):
        '''课程取消再次确认接口'''
        r = req('course/do-class-cancel-confirm', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, reason='123', reasonType='8', secondTime='5933424')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test114(self):
        '''运营红点点击记录'''
        r = req('activity/red-point-count', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1',)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test115(self):
        '''获取用户未读消息列表'''
        r = req('notice/user-unread-notice-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1',)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test116(self):
        '''获取加密后视频地址'''
        r = req('book/get-demo-video', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', songId='5', musicId='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test117(self):
        '''演示视频批量接口'''
        r = req('book/get-batch-demo-video', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', songId='5')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test118(self):
        '''消课排行榜'''
        r = req('book/get-ranking-list', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', page='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test119(self):
        '''视频灰度测试埋点数据'''
        r = req('course/video-gray-log', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, songId='1', eventType='1', musicId='0')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test120(self):
        '''获取进度常量列表'''
        r = req('schedule/get-schedule-enums', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, courseType='1', courseId='34947', classImgName='', scheduleId='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test121(self):
        '''获取某课后单的所有乐谱的课程进度记录列表'''
        r = req('schedule/get-music-list', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test122(self):
        '''获取某乐谱课程进度记录列表'''
        r = req('schedule/get-music-detail', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, courseType='1', courseId='34947', classImgName='', musicName=u'协奏曲1840')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test123(self):
        '''新增课后单课程进度记录'''
        r = req('schedule/add-record', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, instrumentId='1', courseType='1', courseId='34947', classImgName='', courseScope='1.2-2.3', progressId='11', proficiencyId='12', rhythmId='8', speedId='21', intonationId='2226691', skillId='13,12', fingeringId='13,12', bellowsId='13,12', bethId='13,12', variaboxId='13,12', courseOwnName=u'整首乐谱')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test124(self):
        '''更新自定义课程进度乐谱名称'''
        r = req('schedule/update-course-ownname', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, classImgName=u'自主上传乐谱20180620', courseOwnName=u'自定义名称')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test125(self):
        '''删除课后单课程进度记录'''
        r = req('schedule/delete-record', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', scheduleId='22222')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test126(self):
        '''编辑课后单课程进度记录'''
        r = req('schedule/update-record', self.uid, self.accessUser, '0',
                '192.168.56.1', 'sdsdasd', '1', classId=self.classid1, instrumentId='1', courseType='1', courseId='34947', classImgName='', courseScope='1.2-2.3', progressId='11', proficiencyId='12', rhythmId='8', speedId='21', intonationId='2226691', skillId='13,12', fingeringId='13,12', bellowsId='13,12', bethId='13,12', variaboxId='13,12', courseOwnName=u'整首乐谱')
        print r
        self.assertEqual(u'成功', r[u'message'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
