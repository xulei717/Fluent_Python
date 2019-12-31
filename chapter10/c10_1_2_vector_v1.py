# -*- coding:utf-8 -*-
# @time   : 2019-12-18 14:12
# @author : xulei
# @project: Fluent_Python

from array import array
import reprlib
import math


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
        return self._components[index]


    @classmethod
    def frombytes(cls, octets):  # 类方法用classmethod装饰器修饰；通过cls传入类本身
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    print(Vector([3, 4]))
    print(Vector((3, 4, 5)))
    print(Vector(range(10)))
    print(repr(Vector(range(100))))

    '''
    (3.0, 4.0)
    (3.0, 4.0, 5.0)
    (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    '''
    print()
    # x = Vector(range(100))
    x = array('d', range(100))

    from reprlib import Repr
    print(type(x).__name__)
    print(hasattr(Repr, 'repr_' + type(x).__name__))
    print(hasattr(Repr, 'repr_' + 'array'))
    print(reprlib.repr(array('d', range(100))))

    print()
    import builtins

    s = builtins.repr(x)
    print(len(s), s)
    maxother = 60
    if len(s) > maxother:
        i = max(0, (maxother - 3) // 2)
        j = max(0, maxother - 3 - i)
        s = s[:i] + '...' + s[len(s) - j:]
    print(s)

    print()
    from itertools import islice
    print([x for x in islice(x, 5)])
    print([x for x in islice([1, 2, 3], 5)])
    '''
    array
    True
    True
   
    602 array('d', [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0])
    array('d', [0.0, 1.0, 2.0, 3...5.0, 96.0, 97.0, 98.0, 99.0])
    
    [0.0, 1.0, 2.0, 3.0, 4.0]
    [1, 2, 3]
    '''
    print()
    v1 = Vector([3, 4, 5])
    print(len(v1))
    print(v1[0], v1[-1])
    v7 = Vector(range(7))
    print(v7[1:4])
    '''
    3
    3.0 5.0
    array('d', [1.0, 2.0, 3.0])
    '''
