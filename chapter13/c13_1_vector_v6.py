# -*- coding:utf-8 -*-
# @time   : 2019-12-17 14:43
# @author : xulei
# @project: Fluent_Python

import math
from array import array
import itertools


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
