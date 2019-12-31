# -*- coding:utf-8 -*-
# @time   : 2019-12-30 13:52
# @author : xulei
# @project: Fluent_Python


t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))
print(t1 == t2)
'''
True
140179898507144
(1, 2, [30, 40, 99])
140179898507144
False
'''