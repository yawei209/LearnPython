#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#Author: zhangyawei


import pytest

@pytest.fixture(scope="function", params=['张张张','亚亚亚','伟伟伟'])
def my_fixture(request):
    print("这是前置的方法")
    yield request.param
    print("这是后置的方法")

class TestClass:

    def test_01(self,my_fixture):
        name = my_fixture
        print("这是用例一")
        print('------------'+ name)

    def test_02(self):
        print("这是用例二")
