# -*- coding:utf-8 -*-
# @time   : 2019-12-23 16:52
# @author : xulei
# @project: Fluent_Python


# 计算整数0~5的累计异或的3中方式
n = 0
for i in range(1, 6):
    n ^= i
print(n)
print()

import functools
print(functools.reduce(lambda a, b: a ^ b, range(6)))

import operator
print(functools.reduce(operator.xor, range(6)))
"""
1

1
1
"""