# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from BasePage import Page
from homePage import HomePage

class MiaokePage(Page):
    userName_loc = (By.ID, 'username')
    pwd_loc = (By.ID, 'passwd')
    clickButton_loc = (By.PARTIAL_LINK_TEXT, u'登')
    login_loc = (By.ID, 'wechat-info')

    def typeUsername(self):
        self.wait
        self.find_element(*self.userName_loc).send_keys()