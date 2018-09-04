# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# if __name__ == '__main__':
    # receiver = u'hikaruwin@qq.com'
    # sender = u'814360749@qq.com'
    # subject = u'python email文本邮件发送测试'
    # smtpserver = u'smtp.qq.com'
    # username = u'hikaruwin@qq.com'
    # password = u'rkngifikzbgxbiig'
    # msg = MIMEText(u'你好', 'text', 'utf-8')
    # msg['Subject'] = Header(subject, 'utf-8')
    # smtp = smtplib.SMTP()
    # smtp.connect('smtp.qq.com')
    # smtp.login(username, password)
    # smtp.sendmail(sender, receiver, msg.as_string())
    # smtp.quit()
_user = "hikaruwin@qq.com"
_pwd = "rkngifikzbgxbiig"
_to = "hikaruwin@126.com"

msg = MIMEText("Test")
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException, e:
    print "Falied,%s" % e