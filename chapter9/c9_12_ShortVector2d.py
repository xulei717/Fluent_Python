# -*- coding:utf-8 -*-
# @time   : 2019-12-20 14:02
# @author : xulei
# @project: Fluent_Python

from chapter9.c9_7_8_9_10_vector2d_v3 import Vector2d


# 类属性是公开的，因此会被子类继承
class ShortVector2d(Vector2d):
    typecode = 'f'


if __name__ == '__main__':
    sv = ShortVector2d(1/11, 1/27)
    print(sv)
    print(len(bytes(sv)))
    '''
    (0.09090909090909091, 0.037037037037037035)
    9
    '''