#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# def foo():
#     r = some_function()
#     if r ==(-1):
#         return (-1)
#     #do sometiong
#     return r
#
# def bar():
#     r = foo()
#     if r ==(-1):
#         print('Error')
#     else:
#         pass


# try:
#     print('try....')
#     r = 10 / 0
#     print('result', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('tyr...')
#     r = 10 / int('S')
#     print('result', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')


# import  logging
#
# def foo(s):
#     return 10/int(s)
#
# def bar(s):
#     return foo(s)*2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#     finally:
#         print('finally')
#
# main()

# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n ==0:
#         raise FooError("出错了！10不能被0除！！！")
#     return 10/n
# foo('0')

# def foo(s):
#     n = int(s)
#     if n ==0:
#         raise ValueError("出错了！10不能被0除！！！")
#     return 10/n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#
# bar()



# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#
# bar()


# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')


from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
