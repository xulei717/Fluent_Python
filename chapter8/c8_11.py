# -*- coding:utf-8 -*-
# @time   : 2019-12-31 08:50
# @author : xulei
# @project: Fluent_Python


def f(a, b):
    a += b
    return a


x, y = 1, 2
re = f(x, y)
print(id(x), id(y))
print(re, id(re))
print(x, y)
print(id(x), id(y))
print()
'''
9485728 9485760
3 9485792
1 2
9485728 9485760
'''
a = [1, 2]
b = [3, 4]
re1 = f(a, b)
print(id(a), id(b))
print(re1, id(re1))
print(a, b)
print(id(a), id(b))
print()
'''
140459076947848 140459076985224
[1, 2, 3, 4] 140459076947848
[1, 2, 3, 4] [3, 4]
140459076947848 140459076985224
'''
t = (10, 20)
u = (30, 40)
re2 = f(t, u)
print(id(t), id(u))
print(re2, id(re2))
print(t, u)
print(id(t), id(u))
print()
'''
140096971062216 140096971062280
(10, 20, 30, 40) 140096973568344
(10, 20) (30, 40)
140096971062216 140096971062280
'''