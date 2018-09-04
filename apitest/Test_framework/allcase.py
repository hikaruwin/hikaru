# coding:utf-8

from Test_framework.utils.mail import Email
from Test_framework.utils.config import CASE_PATH, REPORT_PATH
import HTMLTestRunner
import unittest2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def all_case():
    # 待执行用例目录
    # case_dir = r"C:\Users\Administrator\apitest\case"
    testcase = unittest2.TestSuite()
    discover = unittest2.defaultTestLoader.discover(CASE_PATH, pattern='tes_baidu.py', top_level_dir=None)
    # discover筛选出来的用例，循环添加到测试套件中去
    # for test_suit in discover:
    #     for test_case in test_suit:
    #         testcase.addTest(test_case)
    testcase.addTests(discover)
    print (testcase)
    return testcase

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    report = REPORT_PATH + '\\report.html'
    # fp = open(report_path, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'接口测试报告', description=u'用例执行情况：')
    # runner.run(all_case())
    # fp.close()
    with open(report, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(f, verbosity=2, title=u'测试报告', description=u'百度用例执行情况：')
        runner.run(all_case())

    # e = Email(title='test_report',
    #           message='test_report',
    #           receiver='hikaruwin@126.com',
    #           server='smtp.qq.com',
    #           sender='hikaruwin@qq.com',
    #           password='rkngifikzbgxbiig',
    #           path=report
    #           )
    # e.send()