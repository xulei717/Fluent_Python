# -*- coding:utf-8 -*-
# @time   : 2019-12-16 17:06
# @author : xulei
# @project: Fluent_Python

"""
1.内置类型（使用C语言编写）的方法不会调用用户定义的类覆盖的特殊方法。

"""


# 内置类型的dict的__init__和__update__方法会忽略我们覆盖的__setitem__方法
class DoppleDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value]*2)


if __name__ == '__main__':
    dd = DoppleDict(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)
'''
{'one': 1}
{'one': 1, 'two': [2, 2]}
{'one': 1, 'two': [2, 2], 'three': 3}
'''