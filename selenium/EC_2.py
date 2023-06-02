#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: zhangyawei

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# WebDriverWait(driver, 10).until(EC.title_is("百度一下，你就知道"))
#
# element = WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(By.ID, 'kw')))
# element.send_keys("测试测试！")

class TestDemo():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        sleep(2)
        self.driver.quit()

    def test_searchinputbox_is_visibility(self):
        self.driver.get('https://www.baidu.com')
        element = self.driver.find_element(By.ID, 'kw')
        result = WebDriverWait(self.driver, 10).until(EC.visibility_of(element)) #如果存在，则返回这个元素。
        result.send_keys('测试测试')
        

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'EC_2.PY'])
