# coding: utf-8
import time
import hashlib
import requests
import json

def crm(starttime):
    # para = {'time_type': '3', 'instrument_id': '1', 'weeks': '1', 'marks': '', 'is_red': '0', 'ttype': '2', 'conflict_id':'0', 'student_id': '97133', 'teacher_id': '8963'}
    para = {'time_type': '3', 'instrument_id': '1', 'weeks': '1', 'marks': '', 'is_red': '0', 'ttype': '0', 'conflict_id': '0', 'student_id': '97133', 'teacher_id': '1913'}
    # para = {'time_type': '3', 'instrument_id': '1', 'weeks': '1', 'marks': '', 'is_red': '0', 'ttype': '0', 'conflict_id': '0', 'student_id': '97083', 'teacher_id': '1915'}
    time_start = {'time_start': starttime}
    datapara = dict(para.items()+time_start.items())
    # print datapara
    # head = {'Cookie': 'PHPSESSID=tbm87sgaf3dpp2d2snbl4iu8ad; _csrf=5ee264bfbb384c69a20363ce6c068c36ced2333c9b4c30c7849076d7cdd45e6fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22tJztxGWMhKRCXvyAQyG7vNLEGCpjw8iH%22%3B%7D; _identity=7d875f3fe6480e6225b00be86f8d7e8f441b99dc9c02dd57910531d58e4683c0a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A48%3A%22%5B961%2C%22DawUTvJ_GQmWj9ZT2gs7cjts7WJXP1rm%22%2C2592000%5D%22%3B%7D'}
    # r = requests.post('http://sales.dev.com:8003/temp-class/do-add-class', headers=head, data=datapara)
    head = {'Cookie': '_csrf=81fa2864330015001e786907e20253a4717f251b58c8604af3c595484373730da%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22d9_Pn8_nuxAl9p-mbuEeu87YGSLpBTdV%22%3B%7D; PHPSESSID=sv8j761jdunvefk6vvmifp6fr0; _identity=ee1762ec2257f683db722fd1b24b48841f96792fb1b5cbdb076a0886cfe6f7aea%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A48%3A%22%5B833%2C%22D4r6UikWIdASGX0k-vptOxucmah51vL6%22%2C2592000%5D%22%3B%7D'}
    r = requests.post('http://vipsales.dev.pnlyy.com/temp-class/do-add-class', headers=head, data=datapara)
    id = r.json()
    print r
    print id
    classid = id[u'data'][u'class_id']
    print classid
    # print r.status_code
    return classid

# crm('2018-2-1 15:00')
