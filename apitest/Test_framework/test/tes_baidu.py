# coding: utf-8

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from Test_framework.utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from Test_framework.utils.log import logger
from Test_framework.utils.file_reader import ExcelReader
import unittest2
from HTMLTestRunner import HTMLTestRunner
from Test_framework.utils.mail import Email
from Test_framework.test.page.baidu_result_page import BaiDuMainPage, BaiDuResultPage

class TestBaiDu(unittest2.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + r'/baidu.xlsx'
    # locator_kw = (By.ID, 'kw')
    # locator_su = (By.ID, 'su')
    # locator_result = (By.XPATH, '//div[contains(@class,"result")]/h3/a')

    def sub_setUp(self):
        # self.driver = webdriver.Firefox()
        # self.driver.get(self.URL)
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search'])
                # self.driver.find_element(*self.locator_kw).send_keys(d[u'search'])
                # self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

    # def test_search_1(self):
    #     self.driver.find_element(*self.locator_kw).send_keys('Java selenium')
    #     self.driver.find_element(*self.locator_su).click()
    #     time.sleep(2)
    #     link = self.driver.find_element(*self.locator_result)
    #     logger.info(link.text)

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title=u'测试报告', description=u'测试结果')
        runner.run(TestBaiDu())
    # e = Email(title='test_report',
    #           message='test_report',
    #           receiver='hikaruwin@126.com',
    #           server='smtp.qq.com',
    #           sender='hikaruwin@qq.com',
    #           password='rkngifikzbgxbiig',
    #           path=report
    #           )
    # e.send()