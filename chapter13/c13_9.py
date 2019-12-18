# -*- coding:utf-8 -*-
# @time   : 2019-12-17 16:00
# @author : xulei
# @project: Fluent_Python

from chapter13.c13_7 import Vector

v1 = Vector([3, 4, 5])
print(v1 + '123')
'''
TypeError: unsupported operand type(s) for +: 'float' and 'str'
'''