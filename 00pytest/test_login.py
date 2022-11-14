#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import pytest
from selenium import webdriver
from time import sleep

class TestCase:

    #先打开浏览器，输入网址
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    #输入框 输入信息
    def test_01(self):
        sleep(1)
        self.driver.find_element_by_id('kw').send_keys("测试通过")
        sleep(1)
        self.driver.find_element_by_id('su').click()
        sleep(2)


    def test_02(self):
        sleep(1)
        self.driver.find_element_by_id('kw').send_keys("测试失败")
        sleep(1)
        self.driver.find_element_by_id('su').click()
        sleep(2)
        assert 1 == 'a'

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_login.py'])