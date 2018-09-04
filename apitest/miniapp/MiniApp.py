# coding: utf-8

import requests

url = 'http://guarder-v1.qa.k8s.pnlyy.com/guarder/v1/class/editClassMark'
headers = {'Content-Type': 'application/json;charset=UTF-8'}
params = {"studentId": 100009, "classId": 2148713,
          "marks": "课程要求测试",
          "classMarkImages": [
              {
                  "classId": 2148713,
                  "path": "class/image/a3ed3fa3eee2d3adafce1ce8a742f6e3",
                  "sort": 0,
                  "adduid": 100009,
                  "rotate": 0},
              {"classId": 2148713,
               "path": "class/image/8d270141e3be0f7470a6d1b00cb2be26",
               "sort": 1,
               "adduid": 100009,
               "rotate": 0},
              {"classId": 2148713,
               "path": "class/image/dc042d20568ef59285644321909b7caf",
               "sort": 2,
               "adduid": 100009,
               "rotate": 0}
          ]}

r = requests.post(url, json=params, headers=headers)
mes = r.json()
print mes[u'msg']

