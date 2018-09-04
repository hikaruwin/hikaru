# coding: utf-8

import requests

url = 'http://httpbin.org/post'
para = {"yoyo":"helloworld", "pythonQQ群":"226296743"}
r = requests.post(url, data=para)

print r.json()