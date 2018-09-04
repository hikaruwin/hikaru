#coding=utf-8
import os, time, sys
import requests                          # 用于发送http请求到蒲公英，第三方模块，需要pip install requests来下载
#import webbrowser                    # 用于打开浏览器，并打开某个网址，系统自带模块
reload(sys)
sys.setdefaultencoding('utf-8')

def IpaCreatedLastly(dir):         # 传入的dir就是文件夹A的路径，如果你的脚本就在当前路径，直接传入“.”即可
    Dirdic={}                            # key＝文件夹名称（包含IPA的文件夹路径），value＝创建的时间
    for i in os.listdir(dir):          # 查找文件夹A中所有的文件
        # print i
        if os.path.isfile(os.path.join(dir, i)):
            # print i
            creattime = os.path.getctime(dir+'\\'+i)  # 算出每个文件夹的创建时间，这里的时间是指距离1970年一月一日的秒数，所以数值越大越说明是最新创建的
            # print creattime
            Dirdic[i] = creattime
            # print Dirdic
    Dirdic = sorted(Dirdic.items(), key=lambda item: item[1], reverse=True)  # 按value值（创建的时间）从大到小对字典排序
    print Dirdic
    DirCreatedLastly = Dirdic[0][0]                                                    # 字典排列的第一的key值，即最新创建的文件夹
    # print DirCreatedLastly
    print '要上传的文件是：'+DirCreatedLastly
    IPAPath= dir+os.sep+DirCreatedLastly
    # for i in os.listdir(dir+'\\'+DirCreatedLastly):                         # 找到该文件路径下面的IPA文件
    #     # if(i.find('.ipa')!=(-1)):
    #     IPAPath=dir+'\\'+DirCreatedLastly+'\\'+i      # 得到最新打包的IPA的夹路径
    #     return IPAPath
    print IPAPath
    return IPAPath

def uploadIPA(IPAPath):
    # IPAPath = IpaCreatedLastly(IPAPath)
    if(IPAPath==''):
        print '未找到对应上传的IPA文件!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        return
    else:
        url = 'https://qiniu-storage.pgyer.com/apiv1/app/upload'         # 上传的url地址
        files = {'file': open(IPAPath, 'rb')}
        # headers = {'enctype': 'multipart/form-data'}
        # headers = {'Content-Type': m.content_type}
        data = {
            'uKey': '55d6f5bb7da4365cf06d09fc003cfcb0',
            '_api_key': '024233dd9ae625bf8bc1ae707d35e699',
            'installType': '1'
            # 'file': files
            }                               #发送的参数数据
        # files = {'file': open(IPAPath, 'rb')}       #上传的文件
        # with open(IPAPath, 'rb') as f:
        r = requests.post(url, data=data, files=files)   # 发送post请求。完事。。。。
        print r.json()
        return r.json()

if __name__ == '__main__':
    uploadIPA(IpaCreatedLastly(u'C:\\Users\\Administrator\\Desktop\\V2.3.1'))
    # IpaCreatedLastly(u'C:\\Users\\Administrator\\Desktop\\V2.3.0')