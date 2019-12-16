# -*- coding:utf-8 -*-
# @time   : 2019-12-12 16:59
# @author : xulei
# @project: Fluent_Python

"""
定义抽象基类的子类
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11) + list('JQKA')]
    suits = 'spadas diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):  # 为了支持洗牌
        self._cards[key] = value

    def __delitem__(self, key):  # MutableSequence类的一个抽象方法
        del self._cards[key]

    def insert(self, index: int, value):  # MutableSequence类的第三个抽象方法
        self._cards.insert(index, value)

