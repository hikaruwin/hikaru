# coding: utf-8

import urllib
import urlparse
import json

# response = urllib.urlopen('http://placekitten.com/g/200/300')
# cat_img = response.read()
# with open('cat_200_300.jpg', 'wb') as f:
#     f.write(cat_img)

content = input(u'请输入需要翻译的内容：')
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'
data = urllib.quote_plus()