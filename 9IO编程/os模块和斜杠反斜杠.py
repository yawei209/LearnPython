#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#Author: zhangyawei

# 斜杠   /	例如linux中路径：/home/root
# 反斜杠 \	例如windows中路径：D:\
#
# 在python中，反斜杠的功能是转义，例如：\n 表示换行；\t 表示制表符也就是tab键；
#
# 如果python字符串想要使用反斜杠字符，可以把反斜杠前转义，就是双反斜杠：’\\‘
# print('\\')
# >>>\
# 也可以在字符长前加上r，告诉pyhton编译器这个字符串是raw string，所有反斜杠\都直接表示，不具备转义功能。
# print(r'\n')
# >>>\n

import os

######斜杠与反斜杠、string.join()、string.split()##########
folder = r'K:\imageData\neg\4'
name = '001.bmp'
path = os.path.join(folder, name)  #重点：os.path.join()
print('path: ',path)

print("以反斜杠\拆分paht：", path.split("\\")) #重点：string.split() 返回拆分后的列表。

path2 = "\\\\".join(path.split('\\')) #重点：string.join，将列表组合成string
print("path2: ", path2) #替换反斜杠\为双反斜杠

path3 = '/'.join(path.split('\\'))
print("path3: ", path3)

# string.split("\")把所有有 \ 的地方断开，返回一个列表


###############################
path = r"K:\imageData\neg\4\001.bmp"
#rsplit("\\",1)把最后出现"\"的地方断开返回一个列表,>>>['K:\\imageData\\neg\\4', '001.bmp']
#rsplit('\\', 2)把右边两个'\'的地方断开，返回一个列表>>>['K:\\imageData\\neg', '4', '001.bmp']

print(path.rsplit('\\', 1))
print(path.rsplit('\\', 2))

#rsplit() 取负数时，相当于split
print(path.rsplit('\\', -1))

#没有lsplit() ?

##############os模块 abspaht#######################

#os.path.abspath(__file__) 作用： 获取当前脚本的完整路径--D:\python_learning\9IO编程\os模块和斜杠反斜杠.py
abspath_file = os.path.abspath(__file__)
print("本目录的绝对路径:\n",abspath_file)

#取同级目录下的另一个文件 cats.txt
abspath_dir = abspath_file.rsplit('\\',1)[0]
print("本文件所在目录的绝对路径:\n",abspath_dir)

abspath_cats = r'{}\cats.py'.format(abspath_dir)
a2 = abspath_dir + '\cats.py' #同
print(abspath_cats)
print(a2)
#取上一级目录下的另一个文件
abspath_parent_dir = abspath_file.split('\\9IO编程')[0]
print("本文件上级目录的绝对路径:\n",abspath_parent_dir)



# format_string = '{}\\config'.format()


abspath_cats3 = r'{}\cats.py'.format(os.path.abspath(__file__).rsplit("\\",1)[0])

print(abspath_cats3)

