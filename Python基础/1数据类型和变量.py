# -*- coding: utf-8 -*-
# @Time : 2022/6/1 20:10
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 1数据类型和变量.py.py
# @Software: PyCharm

#如果字符中又有“ 和’,那要如何实现？可以使用转义字符\来标识
print('I\'m \"OK!\" ')
print('I\'m learning ')
print('\\\n\\')

# r'' 的作用是将''中的转义符都不转移
print(r'\\\n\\')

# 如果需要换行，\n对于观看来说不友好，可以使用""" """ 中间的内容进行换行
print("""line1
line2
line3
""")


print(r"""line1
line2
line3
""")