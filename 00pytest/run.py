#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#生产测试报告
import pytest
import os

if __name__ == '__main__':
    #执行用例生产测试数据
    # pytest.main(['-s', '-v','test_login.py', '--alluredir', './allure-results'])
    pytest.main(['-s', '-v','test_login.py', '--alluredir=report/results'])
    #生成测试报告
    # os.system('allure generate ./allure-results -o ./reports')
    os.system('allure generate report/results -o report/report-html')