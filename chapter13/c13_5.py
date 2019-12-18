# -*- coding:utf-8 -*-
# @time   : 2019-12-17 15:14
# @author : xulei
# @project: Fluent_Python

from chapter13.c13_4 import Vector

v1 = Vector([3, 4, 5])
print(v1 + (10, 20, 30))
print(v1 + (1, 2))
'''
(13.0, 24.0, 35.0)
(4.0, 6.0, 5.0)
'''
