# -*- coding:utf-8 -*-
# @time   : 2019-12-31 10:03
# @author : xulei
# @project: Fluent_Python

import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2, 3, 4}
print(wref())
print(wref() is None)
'''
<weakref at 0x7ffaf477bdb8; to 'set' at 0x7ffaf33d1828>
{0, 1}
None
True
'''
