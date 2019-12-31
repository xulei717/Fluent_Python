# -*- coding:utf-8 -*-
# @time   : 2019-12-30 13:25
# @author : xulei
# @project: Fluent_Python


class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()
try:
    y = Gizmo() * 10
except TypeError as e:
    print(e)
'''
Gizmo id: 140116006392776
Gizmo id: 140116006392944
unsupported operand type(s) for *: 'Gizmo' and 'int'
'''
print(dir())
'''
['Gizmo', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
 '__package__', '__spec__', 'x']
'''