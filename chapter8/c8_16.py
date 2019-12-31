# -*- coding:utf-8 -*-
# @time   : 2019-12-31 09:53
# @author : xulei
# @project: Fluent_Python

import weakref


s1 = {1, 2, 3}
s2 = s1
print(type(s1))  # <class 'set'>


def bye():
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)
'''
True
True
Gone with the wind...
False
'''