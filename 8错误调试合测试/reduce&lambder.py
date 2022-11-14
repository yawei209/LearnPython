#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from functools import reduce

def f(x):
    return x*x

r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r))

L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)

def add(x, y):
    return x+y


print(reduce(add, [1, 3, 5, 7]))


def fn(x,y):
    return x*10 + y

lambda x :x*x