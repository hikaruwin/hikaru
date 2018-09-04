# coding: utf-8

import unittest2
from Test_framework.utils.config import Config, REPORT_PATH
from Test_framework.utils.client import HTTPClient
from Test_framework.utils.log import logger
from HTMLTestRunner import HTMLTestRunner

class TestBaiDuHTTP(unittest2.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        self.assertIn(u'百度一下，你就知道', res.text)

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title=u'测试报告', description=u'测试结果')
        runner.run(TestBaiDuHTTP('TestBaiDuHTTP'))