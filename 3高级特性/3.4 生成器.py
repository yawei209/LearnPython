#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/7/14 12:40
# @Author : zhangyawei
# @Version：V 0.1
# @File : 3.4 生成器.py

g = (x*x for x in range(10))

for n in g:
    print(n)

#斐波那契数列：1，1，2，3，5，8，13，21，34...

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'

fib(10)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

o = fib(5)
print(next(o), next(o))
