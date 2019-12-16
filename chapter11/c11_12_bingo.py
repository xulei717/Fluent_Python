# -*- coding:utf-8 -*-
# @time   : 2019-12-16 14:05
# @author : xulei
# @project: Fluent_Python

import random

from chapter11.c11_9_tombola import Tombola

"""
1.random.SystemRandom()使用os.urandom()函数实现random API.os.random()函数生成“适合用于加密”的随机字节序列。
"""


class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        self.pick()


