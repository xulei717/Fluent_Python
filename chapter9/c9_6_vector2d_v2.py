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
        return '{}({!r}, {!r})'.format(class_name, *self)  # 因为Vector2d实例是可迭代对象，所以self会把x和y分量提供给format函数

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

    def angle(self):  # 计算角度
        return math.atan2(self.y, self.x)

    # 自定义的类型扩展格式规范微语言
    def __format__(self, format_spec=''):  # 可以计算极坐标了
        if format_spec.endswith('p'):  # 格式以'p'结尾，使用极坐标
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())  # 构建一个元组，表示极坐标
            outer_formet = '<{}, {}>'
        else:
            coords = self
            outer_formet = '({}, {})'
        components = (format(c, format_spec) for c in coords)  # 把format_spec应用到向量的各个分量上，构建一个可迭代的格式化字符串
        return outer_formet.format(*components)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(format(v1))
    print(format(v1, '.2f'))
    print(format(v1, '.3e'))
    '''
    3.0, 4.0
    3.00, 4.00
    3.000e+00, 4.000e+00
    '''
    print(format(Vector2d(1, 1), 'p'))
    print(format(Vector2d(1, 1), '.3ep'))
    print(format(Vector2d(1, 1), '0.5fp'))
    print(format(Vector2d(1, 1), '0.5f'))
    '''
    <1.4142135623730951, 0.7853981633974483>
    <1.414e+00, 7.854e-01>
    <1.41421, 0.78540>
    (1.00000, 1.00000)
    '''
    print(abs(Vector2d(1, 1)))
    print(Vector2d(1, 1).angle())
    '''
    1.4142135623730951
    0.7853981633974483
    '''