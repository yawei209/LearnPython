#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# def log(func):
#     def wrapper():
#         print('call %s():' % func.__name__)
#         return func()
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
#
# #使用装饰器，相当于 ：now = log(now)
#
# now()

import time,functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        t1 = time.time()
        fn(*args,**kw)
        t2 = time.time()
        print('%s() executed in %s ms'%(fn.__name__, t2-t1))
        return fn(*args,**kw)
    return wrapper
#测试
@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y
@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z

f=fast(11,22)
s=slow(11,22,33)
if f != 33:
    print('测试失败')
elif s!= 7986:
    print('测试失败')
else:
    print('测试成功')