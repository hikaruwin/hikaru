import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# 员工管理
def Getemployee(driver):
    driver.find_element_by_xpath('ml/body/div[1]/div[1]/div[2]/ul[2]/a').click()
    time.sleep(1)
    # 输入渠道经理姓名
    driver.find_element_by_xpath('//*[@id="employe-keyword"]').click()
    time.sleep(1)
    name = driver.find_element_by_xpath('//*[@id="employe-keyword"]').send_keys('蒋春风')
    driver.find_element_by_xpath('//*[@id="employe-keyword"]').send_keys(Keys.ENTER)
    time.sleep(1)
    name1 = driver.find_element_by_xpath('//*[@id="kefu_4"]/td[2]').text()
    print(name)
    print(name1)
    if name1 == name:
        print('输入的渠道经理姓名,找到了')
    else:
        print('输入的渠道经理姓名,没找到')
        time.sleep(1)
    # 选择状态
    driver.find_element_by_xpath('//*[@id="status"]').click()
    # driver.find_element_by_xpath('//*[@id="status"]').is_selected()
    status = driver.find_element_by_xpath('//*[@id="status"]')
    Select(status).select_by_visible_text('可用')
    time.sleep(1)
    # 点击工作时间
    driver.find_element_by_xpath('//*[@id="work_time"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="work_week"]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="commonModal"]/div/div/div[3]tton[1]').click()
    time.sleep(1)
    # 点击编辑
    driver.find_element_by_xpath('//*[@id=" kefu_4"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="commonModal"]/div/div/div[3]tton[1]').click()
    time.sleep(1)
    # 点击禁用
    # driver.find_element_by_class_name('del label label-warning').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('ml/body/div[4]/div[7]tton').click()

