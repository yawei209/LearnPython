#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: zhangyawei

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
WebDriverWait(driver, 10).until(EC.title_is("百度一下，你就知道"))

element = WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element((By.ID, 'kw'))))
element.send_keys("测试测试！")