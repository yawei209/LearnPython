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

##############pytest.mark.run(order)的用法############

    @pytest.mark.run(order=2)
    def test_01(self):
        print('这是第一条测试用例')
        pass

    @pytest.mark.run(order=1)
    def test_02(self):
        print('这是第二条测试用例')
        pass

#####################################################
    @pytest.mark.pub
    def test_03(self):
        print('这是第三条测试用例')
        pass
    @pytest.mark.pub
    def test_04(self):
        print('这是第四条测试用例')
        pass

    @pytest.mark.skip(reason = "强制跳过test_05了")
    def test_05(self):
        print('这是第5条测试用例')
        pass

    @pytest.mark.skipif(True, reason="有条件跳过test_06了")
    def test_06(self):
        print('这是第6条测试用例')
        pass

#执行用例：1.用命令运行pytest。 2.main方法运行

#pytest.main() 中增加参数 -s、-v 显示详细用例
if __name__ == '__main__':
    pytest.main(['-s','-v','-m' 'pub','test_py.py'])

