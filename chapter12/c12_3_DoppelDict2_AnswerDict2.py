# -*- coding:utf-8 -*-
# @time   : 2019-12-16 17:18
# @author : xulei
# @project: Fluent_Python

import collections

"""
1.因为内置类型的方法通常会忽略用户覆盖的方法。不要子类化内置类型。
2.用户自己定义的类应该继承collections模块中的类，例如UserDict，UserList，UserString，这些类做了特殊设计，因此易于扩展。
"""


class DoppleDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value]*2)


class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42


if __name__ == '__main__':
    dd = DoppleDict2(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)
    '''
    {'one': [1, 1]}
    {'one': [1, 1], 'two': [2, 2]}
    {'one': [1, 1], 'two': [2, 2], 'three': [3, 3]}
    '''

    ad = AnswerDict2(a='foo')
    print(ad['a'])
    d = {}
    d.update(ad)
    print(d)
    '''
    42
    {'a': 42}
    '''
