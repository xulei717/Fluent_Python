# -*- coding:utf-8 -*-
# @time   : 2019-12-18 14:12
# @author : xulei
# @project: Fluent_Python

from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):  # 返回对象的字符串表示形式
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  # 因为Vector2d实例是可迭代对象，所以×self会把x和y分量提供给format函数

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +      # 把typecode转换成字节序列
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)  # 模是x和y分量构成的直角三角形的斜边长

    def __bool__(self):  # 0.0是False，非零值是True
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):  # 类方法用classmethod装饰器修饰；通过cls传入类本身
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)  # *memv得到构造函数所需的一对参数；参数前面加上*号，表示参数的个数不止一个，而且把参数存储为一个元组tuple


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    print(x, y)
    print(v1)
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    print(v1)
    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))
'''
3.0 4.0
3.0 4.0
(3.0, 4.0)
True
(3.0, 4.0)
b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
5.0
True False
'''
