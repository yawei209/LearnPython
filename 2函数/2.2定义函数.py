# -*- coding: utf-8 -*-
# @Time : 2022/6/2 19:41
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 2.2定义函数.py
# @Software: PyCharm

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x


print(my_abs('zyw'))