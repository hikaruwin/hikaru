# coding: utf-8

import requests
import datetime
import time
import threading
import hashlib

class url_request():
    times = []
    error = []

    def req(self, url, uid1, accessUser1, version1, role1, userIp1, requestId1, clientType1, **kw):
        myreq = url_request()
        t = int(time.time())
        uid = {'uid': uid1}
        accessUser = {'accessUser': accessUser1}
        version = {'version': version1}
        role = {'role': role1}
        userIp = {'userIp': userIp1}
        requestId = {'requestId': requestId1}
        clientType = {'clientType': clientType1}
        paramsort = dict(
            uid.items() + accessUser.items() + version.items() + role.items() + userIp.items() + requestId.items() + clientType.items() + {
                'time': str(t)}.items() + kw.items()).items()
        # print paramsort
        paramsort.sort()
        # key = 'jdaDGskjd188ie1w4wirSDew3403sads'

        key = 'ikkkjhgdt6056sdomkn8989mkjjjmmd'  #2.2.0
        # key = 'dasklm974lksadaslhas324jdkldas'  # 2.1.0
        for paramsort1 in paramsort:
            # print paramsort1
            key += paramsort1[1]
        m = hashlib.md5()
        m.update(key)
        mdpaw = m.hexdigest()
        token = {'token': mdpaw}
        # print token
        head = dict(
            uid.items() + accessUser.items() + version.items() + role.items() + userIp.items() + requestId.items() + clientType.items() + {
                'time': str(t)}.items() + token.items())
        # print head
        data = kw
        # print data
        r = requests.post(url, headers=head, data=data)
        m = r.json()
        # print m[u'message']  # 打印接口返回message
        ResponseTime = float(r.elapsed.microseconds) / 1000  # 获取响应时间，单位ms
        myreq.times.append(ResponseTime)  # 将响应时间写入数组
        if m[u'message'] != u'成功':
            myreq.error.append("0")

if __name__ == '__main__':
    myreq = url_request()
    threads = []
    starttime = datetime.datetime.now()
    print "reguest start time %s" %starttime
    nub = 50  # 设置并发线程数
    ThinkTime = 0.5  # 设置思考时间
    for i in range(1, nub + 1):
        t = threading.Thread(target=myreq.req('https://api-dev.pnlyy.com/v4/login/version', '', '', '2.2.0', '0', '192.168.56.1', 'sdsdasd', '1', clientType='1'))
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        print "thread %s" %t  # 打印线程
        t.setDaemon(True)
        t.start()
    t.join()
    endtime = datetime.datetime.now()
    print "request end time %s" % endtime
    time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(myreq.times)) / float(len(myreq.times)))  # 计算数组的平均值，保留3位小数
    print "Average Response Time %s ms" % AverageTime  # 打印平均响应时间
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour) * 60 * 60 + float(minute) * 60 + float(second)  # 计算总的思考时间+请求时间
    print "Concurrent processing %s" % nub  # 打印并发数
    print "use total time %s s" % (totaltime - float(nub * ThinkTime))  # 打印总共消耗的时间
    print "fail request %s" % myreq.error.count("0")  # 打印错误请求数