# -*- coding:utf-8 -*-
# @time   : 2019-12-16 14:05
# @author : xulei
# @project: Fluent_Python

import itertools

from chapter11.c11_9_tombola import Tombola
from chapter11.c11_12_bingo import BingoCage

"""
1.random.SystemRandom()使用os.urandom()函数实现random API.os.random()函数生成“适合用于加密”的随机字节序列。
"""


class AddableBingoCage(BingoCage):

    def __len__(self):
        return len(self._items)

    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):  # 就地运算符：表明会就地修改左操作数，而不会创建新对象作为结果
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self  # 增量赋值特殊方法必须返回self


if __name__ == '__main__':

    vowels = 'DSFAFD'
    globe = AddableBingoCage(vowels)
    # print(globe.inspect())
    # print(globe.pick() in vowels)
    # print(len(globe.inspect()))
    globe2 = AddableBingoCage('XYZ')
    # globe3 = globe + globe2
    # print(len(globe3))
    # print(globe + [10, 20])
    '''
    ('A', 'D', 'D', 'F', 'F', 'S')
    True
    5
    8
    TypeError: unsupported operand type(s) for +: 'AddableBingoCage' and 'list'
    '''
    globe_orig = globe
    print(len(globe_orig.inspect()))
    globe += globe2
    print(len(globe.inspect()))
    globe += ['M', 'N']
    print(len(globe.inspect()))
    print(globe is globe_orig)
    globe += 1
    '''
    6
    9
    11
    True
    TypeError: right operand in += must be 'AddableBingoCage' or an iterable
    '''

