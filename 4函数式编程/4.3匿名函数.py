#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1,20)))
print(L)


L = list(filter((lambda x: x%2==1), range(1,20)))
print(L)
