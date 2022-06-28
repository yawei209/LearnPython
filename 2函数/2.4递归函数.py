# -*- coding: utf-8 -*-
# @Time : 2022/6/13 16:12
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 2.4递归函数.py
# @Software: PyCharm



#通过循环实现：
def fact1(n):
    if n == 1 :
        return 1
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    return sum
print(fact1(1))
print(fact1(5))

#通过递归函数实现
def fact2(n):
    if n == 1:
        return 1
    return n * fact2(n-1)
print(fact2(1))
print(fact2(5))