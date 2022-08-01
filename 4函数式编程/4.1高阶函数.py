#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/7/18 19:04
# @Author : zhangyawei
# @Version：V 0.1
# @File : 4.1高阶函数.py

from functools import reduce

# def f(x):
#     return x * x
# r = map(f, [1,2,3,4,5,6,7,8,9])
# print(list(r))

def fn(x, y):
    return x*10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1,2,3,4,5,6,7,8,9,10])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A','b', None, 'C', ' '])))