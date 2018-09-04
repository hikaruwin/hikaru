# coding: utf-8

import time
import hashlib
import requests
from locust import HttpLocust, TaskSet, task
from case.basetestcase import *

class WebsiteTasks(TaskSet):
    def clientPost(self, url, uid1, accessUser1, version1, role1, userIp1, requestId1, clientType1, **kw):
        t = int(time.time())
        uid = {'uid': uid1}
        accessUser = {'accessUser': accessUser1}
        version = {'version': version1}
        role = {'role': role1}
        userIp = {'userIp': userIp1}
        requestId = {'requestId': requestId1}
        clientType = {'clientType': clientType1}
        paramsort = dict(uid.items() + accessUser.items() + version.items() + role.items() + userIp.items() + requestId.items() + clientType.items() + {'time': str(t)}.items() + kw.items()).items()
        # print paramsort
        paramsort.sort()

        key = 'ikkkjhgdt6056sdomkn8989mkjjjmmd'
        # key = 'dasklm974lksadaslhas324jdkldas'
        for paramsort1 in paramsort:
            # print paramsort1
            key += paramsort1[1]
        m = hashlib.md5()
        m.update(key)
        mdpaw = m.hexdigest()
        token = {'token': str(mdpaw)}
        print token
        head = dict(uid.items() + accessUser.items() + version.items() + role.items() + userIp.items() + requestId.items() + clientType.items() + {'time': str(t)}.items() + token.items())
        print head
        data = kw
        print data
        r = self.client.post(url, headers=head, data=data)
        return r

    def on_start(self):
        r = self.clientPost('/v4/login/login', '', '', '2.2.0', '0', '192.168.56.1', 'sdsdasd', '1', username='14155667788', pwd='123456a', type='0', areaCode='+86', clientId='7d2a1657cdaa35463daa2e773297248a', channelId='5')
        print r
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
        # r = req('/v4/login/login', '', '', '2.2.0', '0', '192.168.56.1', 'sdsdasd', '1',
        #         username='14155667788', pwd='123456a', type='0', areaCode='+86',
        #         clientId='7d2a1657cdaa35463daa2e773297248a', channelId='5')
        # print r
        # print r[u'data']
        # print type(r[u'data'])
        # print (r[u'data'])[u'uid']
        # print type((r[u'data'])[u'uid'])
        # global uid
        # uid = (r['data'])['uid']
        # print uid
        # print type(uid)
        # global accessUser
        # accessUser = (r['data'])['accessToken']
        # print accessUser

    @task(2)
    def index(self):
        self.clientPost('/v4/user/get-user-info', str(uid), str(accessUser), '2.2.0', '0', '192.168.56.1', 'sdsdasd',  '1', channelId='7d2a1657cdaa35463daa2e773297248a', clientId='5')
        # req('/v4/user/get-user-info', str(uid), str(accessUser), '2.2.0', '0', '192.168.56.1',
        #     'sdsdasd', '1', channelId='7d2a1657cdaa35463daa2e773297248a', clientId='5')

    @task(1)
    def about(self):
        self.clientPost('/v4/user/logout', str(uid), str(accessUser), '2.2.0', '0', '192.168.56.1', 'sdsdasd',  '1', udid='7d2a1657cdaa35463daa2e773297248a')
        # req('/v4/user/logout', str(uid), str(accessUser), '2.2.0', '0', '192.168.56.1',
        #     'sdsdasd', '1', udid='7d2a1657cdaa35463daa2e773297248a')

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "https://api-dev.pnlyy.com"
    min_wait = 1000
    max_wait = 5000