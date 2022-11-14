#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()

########################

# def foo(s):
#     n = int(s)
#     #assert后的判断如果是false，就中断程序并抛出异常。
#     assert n != 0, 'n等于0了，没法除'
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()


########################



# import logging
# logging.basicConfig(level=logging.DEBUG)
#
#
#
# s = '1'
# n = int(s)
# logging.info('n = %d' % n)
#
# logging.debug('logging.debug')
# logging.info('logging.info')
# logging.warning('logging.warning')
# logging.error('logging.error')
#
# print(10/n)


########################

import pdb

s = '0'
n = input(s)
pdb.set_trace()
print(10/n)
