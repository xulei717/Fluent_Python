# -*- coding:utf-8 -*-
# @time   : 2019-12-17 15:05
# @author : xulei
# @project: Fluent_Python

from collections import Counter

ct = Counter('safdsafaf')
print(ct)
ct['a'] = -3
ct['s'] = 0
print(ct)
print(+ct)
'''
Counter({'a': 3, 'f': 3, 's': 2, 'd': 1})
Counter({'f': 3, 'd': 1, 's': 0, 'a': -3})
Counter({'f': 3, 'd': 1})
'''

