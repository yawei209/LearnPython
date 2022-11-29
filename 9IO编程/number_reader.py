#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import json

filename = 'number.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)