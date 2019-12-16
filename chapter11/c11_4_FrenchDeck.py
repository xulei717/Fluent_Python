# -*- coding:utf-8 -*-
# @time   : 2019-12-11 16:22
# @author : xulei
# @project: Fluent_Python


import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


if __name__ == '__main__':

    f = FrenchDeck()   # 实现序列的类对象
    print(f)
    print(len(f))
    print([x for x in f])

'''
<__main__.FrenchDeck object at 0x7fd60fc710f0>
52
[Card(rank='2', suit='spades'), Card(rank='2', suit='diamonds'), Card(rank='2', suit='clubs'), Card(rank='2', suit='hearts'), Card(rank='3', suit='spades'), Card(rank='3', suit='diamonds'), Card(rank='3', suit='clubs'), Card(rank='3', suit='hearts'), Card(rank='4', suit='spades'), Card(rank='4', suit='diamonds'), Card(rank='4', suit='clubs'), Card(rank='4', suit='hearts'), Card(rank='5', suit='spades'), Card(rank='5', suit='diamonds'), Card(rank='5', suit='clubs'), Card(rank='5', suit='hearts'), Card(rank='6', suit='spades'), Card(rank='6', suit='diamonds'), Card(rank='6', suit='clubs'), Card(rank='6', suit='hearts'), Card(rank='7', suit='spades'), Card(rank='7', suit='diamonds'), Card(rank='7', suit='clubs'), Card(rank='7', suit='hearts'), Card(rank='8', suit='spades'), Card(rank='8', suit='diamonds'), Card(rank='8', suit='clubs'), Card(rank='8', suit='hearts'), Card(rank='9', suit='spades'), Card(rank='9', suit='diamonds'), Card(rank='9', suit='clubs'), Card(rank='9', suit='hearts'), Card(rank='10', suit='spades'), Card(rank='10', suit='diamonds'), Card(rank='10', suit='clubs'), Card(rank='10', suit='hearts'), Card(rank='J', suit='spades'), Card(rank='J', suit='diamonds'), Card(rank='J', suit='clubs'), Card(rank='J', suit='hearts'), Card(rank='Q', suit='spades'), Card(rank='Q', suit='diamonds'), Card(rank='Q', suit='clubs'), Card(rank='Q', suit='hearts'), Card(rank='K', suit='spades'), Card(rank='K', suit='diamonds'), Card(rank='K', suit='clubs'), Card(rank='K', suit='hearts'), Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

'''