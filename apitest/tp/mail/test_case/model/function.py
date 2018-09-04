# coding: utf-8

from selenium import webdriver
import os
import time as t

# 截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    img_dir = (os.path.join(base_dir, 'report\\image\\'),)
    base = '/'.join(img_dir)
    file_path = base + file_name
    driver.get_screenshot_as_file(file_path)
    print base_dir
    print img_dir
    print base
    print file_path

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver, 'baidu.png')
    driver.quit()