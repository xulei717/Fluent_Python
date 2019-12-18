# -*- coding:utf-8 -*-
# @time   : 2019-12-17 15:48
# @author : xulei
# @project: Fluent_Python

"""
1.如果左操作数是Vector之外的对象，__add__方法无法处理
"""


from chapter13.c13_4 import Vector

v1 = Vector([3, 4, 5])
# print((10, 20, 30) + v1)
'''
Traceback (most recent call last):
  File "/home/xl/CodeStore/Fluent_Python/chapter13/c13_6.py", line 9, in <module>
    print((10, 20, 30) + v1)
TypeError: can only concatenate tuple (not "Vector") to tuple
'''
print(Vector((1, 2)) + v1)
'''
(4.0, 6.0, 5.0)
'''