# coding: utf-8

import requests

def chat(url1, **kw):
    url = 'http://chat.dev.pnlyy.com/v1'+url1
    # print url
    # print type(url)
    chat_token = {'chat_token': 'abc'}
    data = dict(chat_token.items() + kw.items()).items()
    # print type(data)
    print data
    r = requests.post(url, data=data)
    # print r
    # print r.json()[u'msg']
    # print r.json()[u'data'][u'uuid']
    return r.json()

def cget(url1, **kw):
    url = 'http://chat.dev.pnlyy.com/v1'+url1
    chat_token = {'chat_token': 'abc'}
    params = dict(chat_token.items() + kw.items()).items()
    print params
    r = requests.get(url, params=params)
    return r.json()

if '__name__'=='__main__':
    chat('/user/register', acc='testapisum245', app_type='3', keyword='')

