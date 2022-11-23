#!/usr/bin/env python
# _*_ coding: utf-8 _*_

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# print(lines)
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))