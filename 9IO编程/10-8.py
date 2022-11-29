#!/usr/bin/env python
# _*_ coding: utf-8 _*_

files = ['cats.txt', 'dogs1.txt']

for file in files:
    try:
        with open(file) as f_obj:
            contents = f_obj.read()
            pets = contents.split()
            for pet in pets:
                print('My pets are ' + pet.strip())
    except FileNotFoundError:
        # print('Sorry, there is no such file')
        pass
