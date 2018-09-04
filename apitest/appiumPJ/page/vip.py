# coding: utf-8

from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from appiumPJ.page.basePage import BasePage

class vipLogin(BasePage):
    login_loc = (By.ID, 'com.pnlyy.pnlclass.pnlclass_student:id/loginBtn')
    username_loc = (By.ID, 'com.pnlyy.pnlclass.pnlclass_student:id/etUserName')
    passwd_loc = (By.ID, 'com.pnlyy.pnlclass.pnlclass_student:id/etPassword')
    loginButoon_loc = (By.ID, 'com.pnlyy.pnlclass.pnlclass_student:id/btnLogin')

    def clickLogin(self):
        self.wait
        self.find_element(*self.login_loc).click()

    def getUsername(self, username):
        self.wait
        self.find_element(*self.username_loc).send_keys(username)

    def getPasswd(self, passwd):
        self.wait
        self.find_element(*self.passwd_loc).send_keys(passwd)

    def clickLoginButton(self):
        self.wait
        self.find_element(*self.loginButoon_loc).click()

    def login(self, username, passwd):
        self.clickLogin()
        self.getUsername(username)
        self.getPasswd(passwd)
        self.clickLoginButton()