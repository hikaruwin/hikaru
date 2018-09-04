# coding:utf-8

import HTMLTestRunner
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def all_case():
    # 待执行用例目录
    case_dir = r"C:\Users\Administrator\apitest\case"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test_teacher.py', top_level_dir=None)
    # discover筛选出来的用例，循环添加到测试套件中去
    # for test_suit in discover:
    #     for test_case in test_suit:
    #         testcase.addTest(test_case)
    testcase.addTests(discover)
    print (testcase)
    return testcase

if __name__=="__main__":
    # runner = unittest.TextTestRunner()
    report_path = r"C:\Users\Administrator\apitest\case\report\result.html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'接口测试报告', description=u'用例执行情况：')
    runner.run(all_case())
    fp.close()