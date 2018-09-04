# coding: utf-8
import time
import hashlib
import requests


def crmre(reqPhone, reqUser):
    para = {'token': 'xw26ewgj6hojiqw2988'}
    # time_type = '3'
    # instrument_id = '1'
    # weeks = '1'
    # marks = ''
    # is_red = '1'
    # ttype = '1'
    # conflict_id = '1'
    name = {'name': reqUser}
    phone = {'phone': reqPhone}
    # time_start = {'time_start': starttime}
    datapara = dict(para.items()+name.items()+phone.items())
    print datapara
    # paramsort.sort()
    # key = 'dasklm974lksadaslhas324jdkldas'
    # for paramsort1 in paramsort:
    #     key += paramsort1[1]
    # m = hashlib.md5()
    # m.update(key)
    # mdpaw = m.hexdigest()
    # token = {'token': str(mdpaw)}
    # head = dict(uid.items()+accessUser.items()+version.items()+role.items()+userIp.items()+requestId.items()+clientType.items()+{'time': str(t)}.items()+token.items())
    # print head
    # data = kw
    # print data
    # head = {'User-Agent': 'PostmanRuntime/6.2.5',
    #         'cookie': 'PHPSESSID=r9elvoa1b05v1p486qp67ls3a0; _identity=69f9ed17a1480773528d538da552d8ed28b932ff264ac74dc9e5213d0370ee4ea%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A48%3A%22%5B833%2C%22WwhrO2ZQOr3Lz4MndxLOnTjvvWXkLz4f%22%2C2592000%5D%22%3B%7D',
    #         'Authorization': 'Basic emh1aGFuZzoxMjM =',
    #         'accept - encoding': 'gzip, deflate',
    #         'Postman - Token': '222541e4 - dbee - 4c07 - a4a3 - 92f71a4d399e',
    #         'Connection': 'keep - alive',
    #         'Host': 'vipsales.dev.pnlyy.',
    #         'content - length': '136',
    #         'Content - Type': 'application / x - www - form - urlencoded',
    #         'cache - control': 'no - cache',
    #         'Accept': '* / *'
    #         }
    # head = {'Cookie': '_csrf=81fa2864330015001e786907e20253a4717f251b58c8604af3c595484373730da%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22d9_Pn8_nuxAl9p-mbuEeu87YGSLpBTdV%22%3B%7D; PHPSESSID=sv8j761jdunvefk6vvmifp6fr0; _identity=ee1762ec2257f683db722fd1b24b48841f96792fb1b5cbdb076a0886cfe6f7aea%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A48%3A%22%5B833%2C%22D4r6UikWIdASGX0k-vptOxucmah51vL6%22%2C2592000%5D%22%3B%7D'}
    r = requests.post('https://webapi.pnlyy.com/v1/register/test', data=datapara)
    print r.status_code
    print r.json()
    return r.json()
    # print r
    # return r
crmre('18433334444', 'app_测试注册')
    # return r.json()