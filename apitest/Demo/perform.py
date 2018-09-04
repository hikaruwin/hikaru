# coding: utf-8

from selenium import webdriver
import unittest, time

class jsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)

    def test_001(self):
        self.driver.find_element_by_id('kw').send_keys('webdriver')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        js = "var q = document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath(".//*[@id='page']/a[10]").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)