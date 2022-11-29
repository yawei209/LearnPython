#!/usr/bin/env python
# _*_ coding: utf-8 _*_
##############10-6加法运算#############
# try:
#     sum = int(input('Please input your first number:')) + int(input('And input your second number:'))
# except ValueError:
#     print('Sorry worng number!')
# else:
#     print('sum is: '+ str(sum))

#############10-7加法运算器#############

while True:
    """如果try返回错误被except捕获到，责不会到else中，就会在while中一直循环。直到运行成功到else中的break才会跳出循环"""
    try:
        sum = int(input('Please input your first number:')) + int(input('And input your second number:'))
    except ValueError:
        print('Sorry worng number!')
    else:
        print('sum is: ' + str(sum))
        break
#############10-8猫和狗###############