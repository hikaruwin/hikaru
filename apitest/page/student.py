# coding: utf-8

from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from basePage import BasePage

class Student(BasePage):
    phone_loc = (By.ID, 'com.pnlyy.pnlclass.pnlclass_student:id/etUserName')
    paw_loc = (By.ID, 'com.pnlyy.pnlclass.pnlclass_student:id/etPassword')
    loginButton_loc = (By.ID, 'com.pnlyy.pnlclass.pnlclass_student:id/btnLogin')

    def getUsername(self, username):
        self.wait
        self.find_element(*self.phone_loc).send_keys(username)

    def getPassword(self, password):
        self.wait
        self.find_element(*self.paw_loc).send_keys(password)

    def clickLoginButton(self):
        self.wait
        self.find_element(*self.loginButton_loc).click()

    def login(self, username, password):
        self.getUsername(username)
        self.getPassword(password)
        self.clickLoginButton()


