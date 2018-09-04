# coding: utf-8

import unittest, time
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib, os
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# 发送测试报告，需要配置你的邮箱帐号
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['subject'] = Header(u'自动化测试报告', 'utf-8')
    msg['From'] = 'hikaruwin@126.com'
    msg['To'] = '814360749@qq.com'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('hikaruwin', 'zh821218151')
    smtp.sendmail('hikaruwin@126.com', '814360749@qq.com', msg.as_string())
    smtp.quit()
    print('email has send out!')

# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fx: os.path.getmtime(testreport + '\\' + fx))
    file_new = os.path.join(testreport, lists[-1])
    print file_new
    return file_new

# 指定测试用例为当前文件夹下的test_case目录
test_dir = './mail/test_case'
test_report = 'C:\\Users\\Administrator\\apitest\\tp\\mail\\report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_case.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'测试报告',
                            description=u"运行环境：windows 7, Chrome")
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report)