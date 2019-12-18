# -*- coding:utf-8 -*-
# @time   : 2019-12-17 16:00
# @author : xulei
# @project: Fluent_Python

from chapter13.c13_7 import Vector

v1 = Vector([3, 4, 5])
print(v1 + 1)
'''
Traceback (most recent call last):
  File "/home/xl/CodeStore/Fluent_Python/chapter13/c13_8.py", line 9, in <module>
    print(v1 + 1)
  File "/home/xl/CodeStore/Fluent_Python/chapter13/c13_7.py", line 30, in __add__
    pairs = itertools.zip_longest(self, other, fillvalue=0.0)  # zip_longest可以处理任何可迭代对象
TypeError: zip_longest argument #2 must support iteration
'''