# -*- coding:utf-8 -*-
# @time   : 2019-12-23 17:32
# @author : xulei
# @project: Fluent_Python


print(zip(range(5), 'ABC'))
print(list(zip(range(5), 'ABC')))
print(list(zip(range(5), 'ABC', [0, 1, 2, 3])))

from itertools import zip_longest
print(list(zip_longest(range(5), 'ABC', [0, 1, 2, 3])))
"""
<zip object at 0x7f45e6917888>
[(0, 'A'), (1, 'B'), (2, 'C')]
[(0, 'A', 0), (1, 'B', 1), (2, 'C', 2)]
[(0, 'A', 0), (1, 'B', 1), (2, 'C', 2), (3, None, 3), (4, None, None)]
"""