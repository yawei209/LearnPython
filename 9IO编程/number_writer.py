#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import json

number = [2, 3, 5, 7, 11, 13]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    f_obj.write('\n')
    json.dump(number, f_obj)


