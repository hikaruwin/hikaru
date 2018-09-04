# coding: utf-8

import unittest
from case.basetestcase import *
import json


class getVersion(unittest.TestCase):
    verCode2 = ''
    verCode1 = ''
    uid = ''
    accessUser = ''
    # global classid1
    classid1 = '2169523'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01(self):
        '''获取版本信息'''
        r = req('login/version', '', '', '1', '192.168.56.1', 'sdsdasd', '2', clientType='2')
        # clientType手机系统 0ios 1android 2iphone老师
        print r
        print type(r)
        self.assertEqual(u'成功', r[u'message'])

    def test02(self):
        '''用户登录'''
        r = req('hlogin/login', '', '', '1', '192.168.56.1', 'sdsdasd', '2', username='15100000788', pwd='123456', type='2', areaCode='+86', clientId='', channelId='')
        print r
        print type(r)
        self.assertEqual(u'成功', r[u'message'])
        global uid
        uid = (r['data'])['uid']
        print
        global accessUser
        accessUser = (r['data'])['accessToken']
        print accessUser

    def test03(self):
        '''提交调用接口日志信息'''
        r = req('service/set-log', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', content='[\n\t\"7,student,https://xiaohei-api.dev.pnlyy.com/v4/user/is-login,0.169s,0 "\n]')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test04(self):
        '''用户修改设备信息'''
        r = req('https://api-dev.pnlyy.com/v4/user/update-user-device', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', clientID='asdasdas', clientType='2', deviceInfor='fjajf', versionType='0', udid='B7AEA6AC-7C5F-4019-9C74-1BA4C825FC76')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test05(self):
        '''获取分类'''
        r = req('https://api-dev.pnlyy.com/v4/user/category-list', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test06(self):
        '''运营活动弹窗记录'''
        r = req('https://api-dev.pnlyy.com/v4/activity/dialog-count', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', activityNo='VIP20171102199010', type='2')
        print r
        self.assertEqual(u'运营活动不存在', r[u'message'])

    def test07(self):
        '''获取用户信息'''
        r = req('https://api-dev.pnlyy.com/v4/user/get-user-info', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', clientId='', channelId='')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test08(self):
        '''用户退出'''
        r = req('https://api-dev.pnlyy.com/v4/user/logout', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', udid='B7AEA6AC-7C5F-4019-9C74-1BA4C825FC76')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test09(self):
        '''判断用户是否已登入'''
        r = req('https://api-dev.pnlyy.com/v4/user/is-login', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', udid='B7AEA6AC-7C5F-4019-9C74-1BA4C825FC76')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test10(self):
        '''用户详情'''
        r = req('https://api-dev.pnlyy.com/v4/user/get-user-contents', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test11(self):
        '''修改密码'''
        r = req('https://api-dev.pnlyy.com/v4/user/update-password', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', oldPwd='123456', newPwd='123456')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test12(self):
        '''投诉建议'''
        r = req('https://api-dev.pnlyy.com/v4/user/feedback', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', content='极大似乎打算')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test13(self):
        '''修改用户头像'''
        r = req('https://api-dev.pnlyy.com/v4/user/upload-avatar', '1913', '15100000788eacdcaf3c184f1cfa09c2d53d5c0f42b', '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', headName='user/head_icon/20170817115323.jpg')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test14(self):
        '''乐谱库列表'''
        r = req('https://api-dev.pnlyy.com/v4/book/book-list', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', keyword='车尔尼', categoryId='1', page='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test15(self):
        '''乐谱库曲目'''
        r = req('https://api-dev.pnlyy.com/v4/book/catalog', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', keyword='车尔尼', bookId='1', page='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test16(self):
        '''乐谱库曲谱'''
        r = req('https://api-dev.pnlyy.com/v4/book/song-info', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', songId='5')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test17(self):
        '''获取老师课程列表'''
        r = req('home/teacher-home', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', day='5', appTime='150998989988')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test18(self):
        '''获取老师课详情'''
        r = req('home/teacher-detail', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1)
        print self.classid1
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test19(self):
        '''获取课程进度'''
        r = req('https://api-dev.pnlyy.com/v4/course/get-class-schedule', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test20(self):
        '''获取上课乐谱信息'''
        r = req('https://api-dev.pnlyy.com/v4/course/get-image', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test21(self):
        '''获取自主上传的图片信息'''
        r = req('https://api-dev.pnlyy.com/v4/class-image/auto-info', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, name='自主上传乐谱')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test22(self):
        '''添加/删除课乐谱'''
        r = req('https://api-dev.pnlyy.com/v4/class-image/class-song', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, songId='123', type='0')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test23(self):
        '''添加自主上传信息'''
        r = req('https://api-dev.pnlyy.com/v4/class-image/add-auto', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, name='07-31 13:17:02', filePath='[{"rotate":0,"url":"www.baidu.com"},{"rotate":0,"url":"www.baidu.com"}]')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test24(self):
        '''编辑课自主上传图片'''
        r = req('https://api-dev.pnlyy.com/v4/class-image/update-auto', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, name='07-31 13:17:02', filePath='[{"rotate":0,"url":"http://pic.baike.soso.com/ugc/baikepic2/0/ori-20170531213657-819831287.jpg/800"}]')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test25(self):
        '''删除课自主上传图片和添加最近自主上传'''
        r = req('https://api-dev.pnlyy.com/v4/class-image/auto-operate', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, name='07-31 13:17:02', type='1')
        print r
        self.assertEqual(u'成功', r[u'message'])


    def test26(self):
        '''获取七牛的token'''
        r = req('https://api-dev.pnlyy.com/v4/tripartite/get-qiniu-token', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', type='6')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test27(self):
    #     '''学生添加录音'''
    #     r = req('https://api-dev.pnlyy.com/v4/course/save-audio', str(uid), str(accessUser), '2.1.0', '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, audio='reord/audio/cf95cddf810323f4922494816970e877')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test28(self):
        '''获取学生近期的乐谱信息'''
        r = req('https://api-dev.pnlyy.com/v4/class-image/nearest', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', studentId='347')
        print r
        self.assertEqual(u'成功', r[u'message'])


    def test29(self):
        '''获取学生的最新的课后单'''
        r = req('record/near-record', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', studentId='23')
        print r
        self.assertEqual(u'未找到最新的课后单信息', r[u'message'])

    def test30(self):
        '''老师退出教室的理由'''
        r = req('course/out-class', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2',)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test31(self):
        '''呼叫对方'''
        r = req('push/call-dev', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', content='打算大厦将颠', params='', title='标题', type='1', otherUid='6')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test32(self):
        '''保存会议室信息'''
        r = req('course/save-room', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, roomId='1000', roomUrl='www.baidu.com')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test33(self):
        '''保存上课记录信息'''
        r = req('course/class-schedule', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, classStarted='4', nowSongId='', nowSongName='测试1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test34(self):
        '''保存上课录音'''
        r = req('course/save-channel', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, channelId='reord/audio/cf95cddf810323f4922494816970e877')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test35(self):
    #     '''课程线路小开关'''
    #     r = req('https://api-dev.pnlyy.com/v4/course/class-line', str(uid), str(accessUser), '2.1.0', '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, isOpen='0', line='0')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test36(self):
        '''老师获取学生的历史课后单'''
        r = req('record/student-list', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', studentId='46431', page='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test37(self):
        '''获取课后单列表'''
        r = req('record/list', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', recordStatus='0', page='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test38(self):
        '''编辑和添加课后单详情'''
        r = req('record/record-detail', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test39(self):
        '''保存和提交课后单'''
        r = req('record/add-record', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, coherence='1', noteAccuracy='2', performance='3', rhythmAccuracy='4', totalScore='40', process='das', selfAudio='www.baidu.com', audioTime='130', audio='reord/audio/cf95cddf810323f4922494816970e877', image='[{"name":"aaaa","path":[ "www.baidu.com","www.baidu.com"]}]', type='1', tagList='[{"tagCount":10,"tagCode":100},{"tagCount":10,"tagCode":200}]')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test40(self):
        '''编辑课后单'''
        r = req('record/update-record', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', recordId='6891', coherence='1', noteAccuracy='2', performance='3', rhythmAccuracy='4', totalScore='40', process='das', selfAudio='www.baidu.com', audioTime='130', audio='reord/audio/cf95cddf810323f4922494816970e877', image='[{"name":"aaaa","path":[ "www.baidu.com","www.baidu.com"]}]')
        print r
        self.assertEqual(u'课后单不可编辑，请联系管理员', r[u'message'])

    def test41(self):
        '''获取课后单详情'''
        r = req('record/record-info', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, type='1', pageToken='12')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test42(self):
    #     '''记录sdk调用日志'''
    #     r = req('hhttps://api-dev.pnlyy.com/v4/netease/log-error',  '1903', '151000000118ae849cb3de9a52c3ceb631ebeb28d71', '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', userName='15100000011', nickName='测试', reason='缺少xxx', type='1', classId='', code='', classStart='', classEnd='')
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test43(self):
        '''记录课程相关日志信息'''
        r = req('log/class-log', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, type='5')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test44(self):
        '''保存上课中的网络状态'''
        r = req('course/class-net', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, line='1', netDesc='1', userName='ceshi')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test45(self):
        '''获取点赞列表'''
        r = req('open-api/laud-list', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2',)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test46(self):
        '''获取学生对老师的评价标签'''
        r = req('record/tag-list', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', recordId='6891')
        print r
        self.assertEqual(u'此课程，您无权对老师进行评价', r[u'message'])

    def test47(self):
        '''点赞统计'''
        r = req('log/add-laud', str(uid), str(accessUser),  '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1, laudId='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test48(self):
        '''app的系统其它日志'''
        r = req('log/monitor', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', type='1', userTime='1513835476')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test49(self):
        '''app获取h5界面失败日志记录'''
        r = req('log/err-html', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', postUrl='http://baidu.com', postData='', returnData='[{"key":"value"}]')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test50(self):
        '''获取网络信息'''
        r = req('netease/add-network', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId='', context=u'云信很好')
        print r
        self.assertEqual(u'成功', r[u'message'])

    # def test51(self):
    #     '''老师确认固定课时间的变化'''
    #     r = req('https://api-dev.pnlyy.com/v4/push/teacher-execute', str(uid), str(accessUser), '2.2.0', '1', '192.168.56.1', 'sdsdasd', '2', )
    #     print r
    #     self.assertEqual(u'成功', r[u'message'])

    def test51(self):
        '''老师获取更改固定课的时间信息'''
        r = req('push/teacher-execute', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', )
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test52(self):
        '''老师确认固定课时间的变化'''
        r = req('push/execute-read', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', executeTime='12312323433')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test53(self):
        '''教学提示/抽查提示'''
        r = req('course/class-notice', str(uid), str(accessUser), '1', '192.168.56.1', 'sdsdasd', '2', classId=self.classid1)
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test54(self):
        '''获取加密后视频地址'''
        r = req('book/get-demo-video', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', songId='5', musicId='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test55(self):
        '''演示视频批量接口'''
        r = req('book/get-batch-demo-video', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', songId='5')
        print r
        self.assertEqual(u'成功', r[u'message'])

    def test56(self):
        '''获取排行榜'''
        r = req('book/get-ranking-list', str(uid), str(accessUser), '0',
                '192.168.56.1', 'sdsdasd', '1', page='1')
        print r
        self.assertEqual(u'成功', r[u'message'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
