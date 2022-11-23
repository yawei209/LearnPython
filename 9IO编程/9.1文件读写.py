#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# with open('test.txt','r') as f:
#     print(f.read())

#########################################

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.strip())
#

#########################################
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

#########################################
filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming")