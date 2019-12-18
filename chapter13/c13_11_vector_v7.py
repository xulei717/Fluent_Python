# -*- coding:utf-8 -*-
# @time   : 2019-12-17 14:43
# @author : xulei
# @project: Fluent_Python

import math
from array import array
import itertools
import numbers


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):  # 使Vector实例是可迭代的对象
        return iter(self._components)

    def __abs__(self):  # 计算绝对值
        return math.sqrt(sum(x*x for x in self))

    def __neg__(self):  # 计算-v,构建一个新的Vector实例，把self的每个分量都取反
        return Vector(-x for x in self)

    def __pos__(self):  # 计算+v,构建一个新的Vector实例，传入self的每个分量
        return Vector(self)

    def __add__(self, other):  # pairs是生成器，(a, b)形式的元组，a来自self，b来自other。self和other长度不同，使用fillvalue填充那个较短的可迭代对象
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)  # zip_longest可以处理任何可迭代对象
            return Vector(a + b for a, b in pairs)  # 计算pairs中各个元素的和
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __str__(self):  # 实现Vector实例执行print方法时，打印真实的数值元组
        return str(tuple(self))

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Vector(n * other for n in self)
        else:
            return NotImplemented  # 让Python尝试在other操作数上调用__rmul__方法

    def __rmul__(self, other):
        return self * other  # 委托给__mul__方法

    def __matmul__(self, other):
        try:
            return sum(a * b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other


if __name__ == '__main__':
    v1 = Vector([1.0, 2.0, 3.0])
    print(14 * v1)
    print(v1 * True)
    from fractions import Fraction
    print(v1 * Fraction(1, 3))
    '''
    (14.0, 28.0, 42.0)
    (1.0, 2.0, 3.0)
    (0.3333333333333333, 0.6666666666666666, 1.0)
    '''
    from numpy import matrix
    print(matrix([1, 2, 3]) @ matrix([[1], [2], [3]]))  # 矩阵乘法
    '''
    [[14]]
    '''
    print(Vector([1, 2, 3]) @ Vector([1, 1, 1]))
    '''
    6.0
    '''
