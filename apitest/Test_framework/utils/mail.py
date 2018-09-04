# coding: utf-8

import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from Test_framework.utils.log import logger
from Test_framework.utils.config import REPORT_PATH
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Email:
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):

        self.title = title
        self.message = message
        self.files = path
        self.msg = MIMEMultipart('related')
        self.server = server
        self.sender = sender
        self.receiver = receiver
        self.password = password

    def _attach_file(self, att_file):
        att = MIMEText(open('%s' %att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        print att_file
        file_name = re.split(r'[\\|/]', att_file)
        print file_name
        att["Content-Disposition"] = 'attachment; filename="%s"' %file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        if self.message:
            self.msg.attach(MIMEText(self.message))

        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
                    # print f
            elif isinstance(self.files, str):
                self._attach_file(self.files)
                # print self.files

        try:
            smtp_server = smtplib.SMTP_SSL(self.server, 465)
        except (gaierror and error) as e:
            logger.excption(u'发送邮件失败，无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
        else:
            try:
                smtp_server.login(self.sender, self.password)
            except smtplib.SMTPAuthenticationError as e:
                logger.exception(u'用户名密码验证失败！ %s', e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
            finally:
                smtp_server.quit()
                logger.info(u'发送成功'u'{0}'u'成功！ 收件人:{1}。如果没有收到邮件，请检查垃圾箱，同时检查收件人地址是否正确'.format(self.title, self.receiver))

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    # with open(report, 'wb') as f:
        # runner = HTMLTestRunner(f, verbosity=2, title=u'测试报告', description=u'测试结果')
        # runner.run(TestBaiDu('test_search'))
    e = Email(title='test_report',
              message='test_report',
              receiver='hikaruwin@126.com',
              server='smtp.qq.com',
              sender='hikaruwin@qq.com',
              password='rkngifikzbgxbiig',
              path=report
              )
    e.send()