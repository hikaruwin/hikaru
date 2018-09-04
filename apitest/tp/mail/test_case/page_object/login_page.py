# coding: utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from tp.mail.test_case.page_object.base import Base
from selenium import webdriver

# 页面对象登录页面
class LoginPage(Base):
    # base_url =
    login_iframe_loc = 'x-URS-iframe'
    login_mail_button_loc = (By.ID, 'lbNormal')
    login_username_text_loc = (By.NAME, 'email')
    login_password_text_loc = (By.NAME, 'password')
    login_button_loc = (By.ID, 'dologin')
    login_erro_hint_loc = (By.CLASS_NAME, 'ferrorhead')

# 把每一个元素封装成一个方法
    def login_iframe(self):
        self.iframe(self.login_iframe_loc)
        sleep(2)

    def login_iframe_out(self):
        self.iframe_out()

    def login_mail_button(self):
        self.find_element(*self.login_mail_button_loc).click()

    def login_username(self, text):
        self.driver.find_element(*self.login_username_text_loc).send_keys(text)

    def login_password(self, text):
        self.driver.find_element(*self.login_password_text_loc).send_keys(text)

    def login_button(self):
        self.driver.find_element(*self.login_button_loc).click()

    def login_error_hint(self):
        self.login_iframe()
        return self.find_element(*self.login_erro_hint_loc).text
        self.login_iframe_out()

    def login_action(self, username, password):
        # self.login_mail_button()
        sleep(5)
        self.login_iframe()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        self.login_iframe_out()

if __name__ == '__main__':
    url = 'http://mail.163.com'
    driver = webdriver.Chrome()
    ob = LoginPage(driver, url, u'网易')
    ob.open()
    ob.login_action('', '')
    driver.quit()
