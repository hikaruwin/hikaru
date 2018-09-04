# coding: utf-8

import unittest
from chatApi import chat
from chatApi import cget

class uset(unittest.TestCase):
    acc_user = 'testuser132'
    acc_kefu = 'testkefu132'
    # user_uuid = ''
    # kefu_uuid = ''
    # user_client_id = ''
    # chat_id = ''
    # link_id = ''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test001(self):
        '''创建用户uuid'''
        r = chat('/user/register', acc=self.acc_user)
        print r
        self.assertEqual(0, r[u'error'])
        # global user_uuid
        # user_uuid = r[u'data'][u'uuid']
        # print user_uuid

    def test002(self):
        '''更新用户uuid'''
        r = chat('/user/update', acc=self.acc_user)
        print r
        self.assertEqual(0, r[u'error'])
        global user_uuid
        user_uuid = str(r[u'data'][u'uuid'])
        print user_uuid

    def test003(self):
        '''更新用户信息'''
        r = chat('/user/update-info', uuid=user_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    def test004(self):
        '''更新正在等待的用户类型'''
        r = chat('/user/update-user-param', uuid=user_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    def test005(self):
        '''创建客服'''
        r = chat('/kefu/register', acc=self.acc_kefu)
        print r
        self.assertEqual(0, r[u'error'])
        # global kefu_uuid
        # kefu_uuid = r[u'data'][u'uuid']
        # print kefu_uuid

    def test006(self):
        '''更新客服uuid'''
        r = chat('/kefu/update', acc=self.acc_kefu)
        print r
        self.assertEqual(0, r[u'error'])
        global kefu_uuid
        kefu_uuid = str(r[u'data'][u'uuid'])
        print kefu_uuid

    def test007(self):
        '''更新客服信息'''
        r = chat('/kefu/update-info', uuid=kefu_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    def test008(self):
        '''获取所有在线客服'''
        r = cget('/kefu/get-online-kefu')
        print r
        self.assertEqual(0, r[u'error'])
        global kefu_uuid
        kefu_uuid = str(r[u'data'][0][u'uuid'])
        global user_client_id
        user_client_id = str(r[u'data'][0][u'client_id'])
        print kefu_uuid
        print user_client_id
        # if r[u'data']!=u'':
        #     list_data=r[u'data']
        #     for i in list_data:
        #         if i[u'uuid']!=u'':
        #             uuid_resault=i[u'uuid']
        #             print uuid_resault
        #         if i[u'client_id']!=u'':
        #             client_id_resault=i[u'client_id']
        #             print client_id_resault
        #             print ''

    def test009(self):
        '''客服某天内接待客服的数量'''
        r = cget('/kefu/get-kefu-access', kefu_uuid=kefu_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    def test010(self):
        '''检查客服是否连接服务'''
        r = cget('/link/check-con', kefu_uidd=kefu_uuid)
        print r
        self.assertEqual(0, r[u'error'])
        global user_client_id
        user_client_id = str(r[u'data'][u'client_id'])
        print user_client_id

    def test011(self):
        '''客户端关闭连接'''
        r = cget('/link/close-con', client_id=user_client_id)
        print r
        self.assertEqual(0, r[u'error'])

    def test012(self):
        '''获取用户是否和客服连接接口'''
        r = cget('/link/check-user-link', uuid=user_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    def test013(self):
        '''获取连接中用户列表'''
        r = cget('/chat/get-inline-user-list', client_id=user_client_id)
        print r
        self.assertEqual(0, r[u'error'])

    def test014(self):
        '''获取历史接待用户列表'''
        r = cget('/chat/get-offline-user-list', uuid=kefu_uuid)
        print r
        self.assertEqual(0, r[u'error'])
        global link_id
        link_id = str(r[u'data'][u'user_list'][0][u'link_id'])
        user_uuid = r[u'data'][u'user_list'][0][u'uuid']
        print link_id
        print user_uuid

    def test015(self):
        '''获取历史消息列表'''
        r = cget('/chat/get-message-list', user_uuid=user_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    def test016(self):
        '''app获取历史消息列表'''
        r = cget('/chat/app-get-message-list', user_uuid=user_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    def test017(self):
        '''app获取是否有未读消息'''
        r = cget('/chat/check-unread', user_uuid=user_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    def test018(self):
        '''app获取是否有未读消息'''
        r = cget('/chat/check-unread', user_uuid=user_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    # def test019(self):
    #     '''获取客服未读消息列表'''
    #     r = cget('/chat/get-pre-message-list', user_uuid=user_uuid)
    #     print r
    #     self.assertEqual(0, r[u'error'])

    def test020(self):
        '''根据参数获取等待用户数'''
        r = cget('/chat/get-wait-count')
        print r
        self.assertEqual(0, r[u'error'])

    # def test021(self):
    #     '''根据参数获取等待用户数'''
    #     r = cget('/chat/get-wait-count')
    #     print r
    #     self.assertEqual(0, r[u'error'])

    # def test022(self):
    #     '''根据参数获取等待用户列表'''
    #     r = cget('/chat/get-wait-list')
    #     print r
    #     self.assertEqual(0, r[u'error'])

    def test023(self):
        '''获取有已读消息未被回复的用户,is_connect为1时连接，为0时未连接'''
        r = cget('/chat/get-unreply-user', user_uuid=user_uuid, kefu_uuid=kefu_uuid, is_connect='0')
        print r
        self.assertEqual(0, r[u'error'])

    def test024(self):
        '''接入用户'''
        r = chat('/chat/access', user_uuid=user_uuid, kefu_uuid=kefu_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    # def test025(self):
    #     '''接入用户'''
    #     r = chat('/chat/access', user_uuid=user_uuid, kefu_uuid=kefu_uuid)
    #     print r
    #     self.assertEqual(0, r[u'error'])

    def test026(self):
        '''发送回执'''
        r = chat('/chat/receipt', user_uuid=user_uuid, kefu_uuid=kefu_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    def test027(self):
        '''app取消新消息小蓝点'''
        r = chat('/chat/cancel-new-message', user_uuid=user_uuid)
        print r
        self.assertEqual(0, r[u'error'])

    def test028(self):
        '''用户发送文字消息'''
        r = chat('/message/user-add-text-message', uuid=user_uuid, text='124')
        print r
        self.assertEqual(0, r[u'error'])

    def test029(self):
        '''用户发送图片消息'''
        r = chat('/message/user-add-image-message', uuid=user_uuid, path='http://www.baidu.com')
        print r
        self.assertEqual(0, r[u'error'])

    def test030(self):
        '''用户发送语音消息'''
        r = chat('/message/user-add-voice-message', uuid=user_uuid, path='http://www.baidu.com')
        print r
        self.assertEqual(0, r[u'error'])

    def test031(self):
        '''发送系统消息'''
        r = chat('/message/add-system-message', uuid=user_uuid, text='124')
        print r
        self.assertEqual(0, r[u'error'])
        global chat_id
        chat_id = str(r[u'data'][u'chat_id'])
        print chat_id

    def test032(self):
        '''标记系统消息为已处理'''
        r = chat('/message/process-system-message', chat_id=chat_id)
        print r
        self.assertEqual(0, r[u'error'])

    def test033(self):
        '''同步聊天记录'''
        r = chat('/message/sync-message', uuid_from=user_uuid, uuid_to='0956819d-d98f-ddb9-156d-e5d024092566')
        print r
        self.assertEqual(0, r[u'error'])

    def test034(self):
        '''获取表情列表'''
        r = cget('/face/get-face-list')
        print r
        self.assertEqual(0, r[u'error'])

    def test035(self):
        '''添加表情'''
        r = chat('/face/add-face', emoji='/jgjg', image_path='http://www.baidu.com')
        print r
        self.assertEqual(0, r[u'error'])

    def test036(self):
        '''退出接待'''
        r = chat('/chat/off-chat', link_id=link_id)
        print r
        self.assertEqual(50011, r[u'error'])