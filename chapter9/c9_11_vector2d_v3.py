# -*- coding:utf-8 -*-
# @time   : 2019-12-18 14:12
# @author : xulei
# @project: Fluent_Python

from array import array
import math


class Vector2d:
    __slots__ = ('__x', '__y')  # 目的是告诉解释器：这个类中的所有实例属性都在这儿了，比使用__dict__节省了大量的内存，尤其是有数百万个属性或者是数百万个实例同时运行

    typecode = 'd'  # 8字节双精度浮点数

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):  # @property装饰器把读值方法标志为特性
        return self.__x

    @property
    def y(self):  # 这样的Vector.y是只读特性，在外部不可改变，只有这样才能实现__hash__方法
        return self.__y

    def __hash__(self):  # 有个这个方法，向量就可以变成散列的了
        return hash(self.x) ^ hash(self.y)  # 使用位运算符 异或^ 混合各分量的散列值

    def __iter__(self):  # 通过self.x读取公开特性，而不必读取私有属性
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
    v2 = Vector2d(3.1, 4.2)
    print(v1)  # str
    print(repr(v1))  # __repr__
    print(hash(v1), hash(v2))
    print(set([v1, v2]))
    # v1.x = 2
    '''
    (3.0, 4.0)
    Vector2d(3.0, 4.0)
    7 384307168202284039
    {Vector2d(3.1, 4.2), Vector2d(3.0, 4.0)}
    Traceback (most recent call last):
      File "/home/xl/CodeStore/Fluent_Python/chapter9/c9_7_vector2d_v3.py", line 78, in <module>
        v1.x = 2
    AttributeError: can't set attribute
    '''
    print(v1.__slots__)
    '''
    ('__x', '__y')
    '''
    print(v1._Vector2d__x)
    '''
    3.0
    '''


