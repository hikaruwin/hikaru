# coding: utf-8
import time
import hashlib
import requests
import json

def crmCn(classid):
    para = {'cancel_type': '0', 'content': 'ceshi', 'cancel_count': '1', 'current_time': '0', 'is_reduce': '0'}
    class_id = {'class_id': classid}
    datapara = dict(para.items()+class_id.items())
    # print datapara
    # head = {'Cookie': 'PHPSESSID=tbm87sgaf3dpp2d2snbl4iu8ad; _csrf=5ee264bfbb384c69a20363ce6c068c36ced2333c9b4c30c7849076d7cdd45e6fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22tJztxGWMhKRCXvyAQyG7vNLEGCpjw8iH%22%3B%7D; _identity=7d875f3fe6480e6225b00be86f8d7e8f441b99dc9c02dd57910531d58e4683c0a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A48%3A%22%5B961%2C%22DawUTvJ_GQmWj9ZT2gs7cjts7WJXP1rm%22%2C2592000%5D%22%3B%7D'}
    # r = requests.post('http://sales.dev.com:8003/temp-class/do-cancel-class', headers=head, data=datapara)
    head = {'Cookie': '_csrf=81fa2864330015001e786907e20253a4717f251b58c8604af3c595484373730da%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22d9_Pn8_nuxAl9p-mbuEeu87YGSLpBTdV%22%3B%7D; PHPSESSID=mcegmgc3od58cq1tc0tlkk0271; _identity=69f9ed17a1480773528d538da552d8ed28b932ff264ac74dc9e5213d0370ee4ea%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A48%3A%22%5B833%2C%22WwhrO2ZQOr3Lz4MndxLOnTjvvWXkLz4f%22%2C2592000%5D%22%3B%7D'}
    r = requests.post('http://vipsales.dev.pnlyy.com/temp-class/do-cancel-class', headers=head, data=datapara)

    rs = r.json()
    print rs
    if rs[u'error']=='':
        print u'取消成功'
    else:
        print u'取消失败'

# crmCn(118818976)