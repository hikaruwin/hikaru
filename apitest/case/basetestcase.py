# coding: utf-8
import time
import hashlib
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# def paramssort(**a):
#     t = int(time.time())
#     it = (kw.items()+{'time': str(t)}.items())
#     # it = dt.items()
#     it.sort()
#     string = 'dasklm974lksadaslhas324jdkldas'
#     for it1 in it:
#         string+=it1[1]
#     print string
#     print type(string)
#     return string
#
# def head(**b):
#     return dict(b.items() + paw1.items())
#
# def data(**c):
#     return c
# class baseTestCase():

# 接口请求函数
def req(url, uid1, accessUser1, role1, userIp1, requestId1, clientType1, **kw):
    url = r'https://api-dev.pnlyy.com/v5/'+url  # 测试环境
    # url = r'https://api-pre.pnlyy.com/v5/'+url  # 预发环境
    # url = r'https://api4.pnlyy.com/v5/'+url  # 正式环境
    # print url
    t = int(time.time())
    uid = {'uid': uid1}
    accessUser = {'accessUser': accessUser1}
    version = {'version': '2.3.2'}
    role = {'role': role1}
    userIp = {'userIp': userIp1}
    requestId = {'requestId': requestId1}
    clientType = {'clientType': clientType1}
    paramsort = dict(uid.items()+accessUser.items()+version.items()+role.items()+userIp.items()+requestId.items()+clientType.items()+{'time': str(t)}.items()+kw.items()).items()
    # print paramsort
    paramsort.sort()
    # key = '459626a6866fb1d140705dadd0c6249c'  # 2.4.0
    key = '9f9032a0136b7d3224d6e34db7c35f9b'  # 2.3.0
    # key = 'jdaDGskjd188ie1w4wirSDew3403sads'  # 2.2.3

    # key = 'ikkkjhgdt6056sdomkn8989mkjjjmmd'  # 2.2.0
    # key = 'dasklm974lksadaslhas324jdkldas'  # 2.1.0
    for paramsort1 in paramsort:
        # print paramsort1
        key += paramsort1[1]
    m = hashlib.md5()
    m.update(key)
    mdpaw = m.hexdigest()
    token = {'token': mdpaw}
    print token
    head = dict(uid.items()+accessUser.items()+version.items()+role.items()+userIp.items()+requestId.items()+clientType.items()+{'time': str(t)}.items()+token.items())
    print head
    data = kw
    print data
    r = requests.post(url, headers=head, data=data)
    # print r.json()
    return r.json()

# print req('https://xiaohei-api.dev.pnlyy.com/v4/login/version', '', '', '2.2.0', '1', '192.168.56.1', 'sdsdasd', '1', clientType='1')
