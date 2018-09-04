# coding: utf-8

from selenium import webdriver
import time

def login(driver):
    driver.maximize_window()
    driver.get('http://vipchannel.dev.pnlyy.com/')
    time.sleep(2)
    driver.find_element_by_id('username').send_keys('jiangchunfeng')
    driver.find_element_by_id('passwd').send_keys('123')
    time.sleep(2)
    driver.find_element_by_xpath('.//*[@id="loginbox"]/div[5]/div/div/input').click()
    time.sleep(5)
    driver.find_element_by_xpath('html/body/div[1]/div[1]/div[1]/img').click()
    time.sleep(2)
    driver.find_element_by_link_text(u'用户名单').click()
    time.sleep(5)


def Getuserlist(driver):
    # driver = webdriver.Chrome()

    # 点击伸展图标
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/img").click()
    time.sleep(1)
    # 点击伸缩图标
    # time.sleep(1)
    #  driver.find_element_by_xpath("//*[@id='hideMenu']/span").click()

    # 点击用户名单菜单
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/ul/li[1]/a").click()
    time.sleep(1)

    # 用户名单页面输入老师姓名回车搜索
    name = driver.find_element_by_xpath('//*[@id="search_name"]').send_keys('哒哒')
    driver.find_element_by_xpath('//*[@id="search_name"]').send_keys(Keys.ENTER)  # 回车

    # //*[@id="detailPage"]/table/tbody/tr[1]/td[1]/li[2]
    if driver.find_element_by_xpath('//*[@id="detailPage"]/table/tbody/tr[1]/td[1]/li[2]').text == name:
        assert ''
    else:
        assert''

    time.sleep(1)

    # 点击推广用户tab
    driver.find_element_by_xpath('//*[@id="channel_user_2"]/a').click()
    time.sleep(1)

    # 点击无价值用户tab
    driver.find_element_by_xpath('//*[@id="useless_user_3"]/a').click()
    time.sleep(1)

    # 点击我的名单tab
    driver.find_element_by_xpath('//*[@id="useless_user_4"]/a').click()
    time.sleep(1)

    # 点击奖励名单提醒tab
    driver.find_element_by_xpath('//*[@id="useless_user_5"]/a').click()
    time.sleep(1)

    # 点击每日聊通tab
    driver.find_element_by_xpath('//*[@id="useless_user_6"]/a').click()
    time.sleep(1)

    # 继续在用户名单-新用户tab输入老师手机号回车搜索
    driver.find_element_by_xpath('//*[@id="new_user_1"]/a').click()
    driver.find_element_by_xpath('//*[@id="search_name"]').clear()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="search_name"]').send_keys('15940277230')
    driver.find_element_by_xpath('//*[@id="search_name"]').send_keys(Keys.ENTER)
    time.sleep(1)

    # 点击推广用户tab
    driver.find_element_by_xpath('//*[@id="channel_user_2"]/a').click()
    time.sleep(1)

    # 点击无价值用户tab
    driver.find_element_by_xpath('//*[@id="useless_user_3"]/a').get_attribute()
    time.sleep(1)

    # 点击我的名单tab
    driver.find_element_by_xpath('//*[@id="useless_user_4"]/a').click()
    time.sleep(1)

    # 点击奖励名单提醒tab
    driver.find_element_by_xpath('//*[@id="useless_user_5"]/a').click()
    driver.find_element_by_xpath('//*[@id="search_name"]').clear()

    # dates = driver.find_element_by_xpath('//*[@id="search_date_1"]')
    reward = driver.find_element_by_xpath('//*[@id="reward_type"]')
    Select(reward).select_by_visible_text("体验达人奖")

    time.sleep(1)

    # 点击每日聊通tab
    driver.find_element_by_xpath('//*[@id="useless_user_6"]/a').click()
    time.sleep(1)

    # 点击新用户用户tab
    driver.find_element_by_xpath('//*[@id="new_user_1"]/a').click()
    driver.find_element_by_xpath('//*[@id="search_name"]').clear()
    time.sleep(1)

    #  继续在新用户tab中输入学生手机号作为单独条件回车搜索
    driver.find_element_by_xpath('//*[@id="student_phone"]').send_keys('18317172276')
    driver.find_element_by_xpath('//*[@id="student_phone"]').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="student_phone"]').clear()
    driver.quit()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    login(driver)
    Getuserlist(driver)