#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#Author: zhangyawei

# test_setup.py文件的内容

import pytest


def setup_module():
    print("模块级别：在整个.py模块开始前只执行一起")


def teardown_module():
    print("模块级别：在整个.py模块结束后只执行一次")


def setup_function():
    print("函数级别：在每个函数级别用例开始前都执行一次")


def teardown_function():
    print("函数级别：在每个函数级别用例结束后都执行一次")


def test_one():
    print("函数一")


def test_two():
    print("函数二")


class TestSetup():

    def setup_class(self):
        print("类级别：在整个测试类开始前只执行一次")

    def teardown_class(self):
        print("类级别：在整个测试类结束后只执行一次")

    def setup_method(self):
        print("方法级别：在测试类里面每个测试用例开始前都执行一次")

    def teardown_method(self):
        print("方法级别：在测试类里面每个测试用例结束后都执行一次")

    def setup(self):
        print("方法细化级别：在测试类里面每个测试用例开始前都执行一次")

    def teardown(self):
        print("方法细化级别：在测试类里面每个测试用例结束后都执行一次")

    def test_three(self):
        print("方法一")

    def test_four(self):
        print("方法二")
