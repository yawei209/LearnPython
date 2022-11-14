#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#pytest的规则
#1.测试文件以test_开头（或者以_test结尾）
#2.测试类以Test开头，并且不能带有init方法
#3.测试函数以test_开头
#4.断言使用assert

import pytest

class Testcase:

    # def setup_class(self):
    #     print("所有用例执行之前的setup")
    #
    # def teardown_class(self):
    #     print("所有用例执行完后的teardown")
    #
    # def setup(self):
    #     print('这是用例执行之前的setup')
    #
    # def teardown(self):
    #     print('这是用例执行之后的teardown')

    @pytest.mark.run(order=2)
    def test_01(self):
        # print('这是第一条测试用例')
        # assert 1 == 12
        pass

    @pytest.mark.run(order=1)
    def test_02(self):
        # print('这是第二条测试用例')
        # assert 1 == '1'
        pass

#执行用例：1.用命令运行pytest。 2.main方法运行

#pytest.main() 中增加参数 -s、-v 显示详细用例
if __name__ == '__main__':
    pytest.main(['-s','-v','test_py.py'])

