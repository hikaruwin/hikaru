# coding: utf-8

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
#
# # 等待方法
# def wait():
#     t.sleep(5)
#
# def clickLogin(driver):
#     wait()
#     driver.find_element_by_link_text(u'登录').click()
#
# def typeUsername(driver, username):
#     # clickLogin(driver)
#     wait()
#     driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys(username)
#
# def typePassword(driver, password):
#     # clickLogin(driver)
#     wait()
#     driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys(password)
#
# def clickButtonLogin(driver):
#     wait()
#     driver.find_element_by_id('TANGRAM__PSP_3__submit').click()
#
# def getErrorText(driver):
#     wait()
#     return driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_3__error']").text
#
# # 登录方法
# def login(driver, username, password):
#     clickLogin(driver)
#     typeUsername(driver, username)
#     typePassword(driver, password)
#     clickButtonLogin(driver)
#
# # 获取昵称方法
# def getNiCheng(driver):
#     wait()
#     return driver.find_element_by_xpath(".//*[@id='s_username_top']/span").text
#
# # 退出方法
# def exit(driver):
#     wait()
#     move = driver.find_element_by_xpath(".//*[@id='s_username_top']/span")
#     ActionChains(driver).move_to_element(move).perform()
#     wait()
#     driver.find_element_by_xpath(".//*[@id='s_user_name_menu']/div/a[5]").click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from BasePage import Page
from homePage import HomePage

class BaiduPage(Page):
    click_loc = (By.LINK_TEXT, u'登录')
    userName_loc = (By.ID, 'TANGRAM__PSP_3__userName')
    password_loc = (By.ID, 'TANGRAM__PSP_3__password')
    clickButton_loc = (By.ID, 'TANGRAM__PSP_3__submit')
    error_loc = (By.XPATH, ".//*[@id='TANGRAM__PSP_3__error']")

    def click(self):
        self.wait
        self.find_element(*self.click_loc).click()

    def getUserTextField(self, username):
        self.wait
        self.find_element(*self.userName_loc).send_keys(username)

    def getPasswordField(self, password):
        self.wait
        self.find_element(*self.password_loc).send_keys(password)

    def getSubmitButton(self):
        self.wait
        self.find_element(*self.clickButton_loc).click()

    def getLoginErrorDiv(self):
        self.wait
        return self.find_element(*self.error_loc).text

    def login(self, username, password):
        self.doLogin(username, password)
        return HomePage(self.driver)

    def doLogin(self, username, password):
        self.click()
        self.getUserTextField(username)
        self.getPasswordField(password)
        self.getLoginErrorDiv()



