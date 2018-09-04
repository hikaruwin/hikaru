# coding: utf-8

import time


def ti(data):
    data1 = time.mktime(time.strptime(data, '%Y-%m-%d %H:%M'))
    data2 = data1+3600
    data3 = time.strftime('%Y-%m-%d %H:%M', time.localtime(data2))
    print data3
    return data3

# ti('2018-1-29 12:00')