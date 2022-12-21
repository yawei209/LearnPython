#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#Author: zhangyawei

import sys
for a in sys.stdin:
    a = int(a)
    if a%2:
        print("奇数\n")
    else:
        print("偶数\n")