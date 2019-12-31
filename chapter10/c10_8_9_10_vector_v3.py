# -*- coding:utf-8 -*-
# @time   : 2019-12-18 14:12
# @author : xulei
# @project: Fluent_Python

from array import array
import reprlib
import math
import numbers


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):  # 返回对象的详细信息的字符串表示形式
        components = reprlib.repr(self._components)  # 使用reprlib.repr获得self._componets的有限长度表示形式
        components = components[components.find('['):-1]  # 去掉前面的array('d'和后面的)
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +      # 把typecode转换成字节序列
                bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):  # 0.0是False，非零值是True
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])  # 构建一个新的Vector实例
        elif isinstance(index, numbers.Integral):  # numbers.Integral是一个抽象基类
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):  # 仅当对象没有指定名称的属性时，才会调用这个方法，这是一种后备机制
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos <= len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():  # 为所有小写字母的属性设置一个错误消息
                error = "can't set atttibutes 'a' to 'z' in {cls-name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    @classmethod
    def frombytes(cls, octets):  # 类方法用classmethod装饰器修饰；通过cls传入类本身
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v7 = Vector(range(7))
    print(v7[-1])
    print(v7[1:4])
    print(v7[-1:])
    # print(v7[1, 2])
    """
    6.0
    (1.0, 2.0, 3.0)
    (6.0,)
    TypeError: Vector indices must be integers
    """
    print()
    v = Vector(range(5))
    print(v)
    print(v.x)
    v.x = 10
    print(v.x)
    print(v)
    """
    (0.0, 1.0, 2.0, 3.0, 4.0)
    0.0
    10
    (0.0, 1.0, 2.0, 3.0, 4.0)
    """
