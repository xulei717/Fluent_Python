# -*- coding:utf-8 -*-
# @time   : 2019-12-11 16:32
# @author : xulei
# @project: Fluent_Python

from random import shuffle
from chapter11.c11_4_FrenchDeck import FrenchDeck

deck = FrenchDeck()


def set_card(deck, position, card):
    deck._cards[position] = card


FrenchDeck.__setitem__ = set_card


shuffle(deck)
print(deck[:5])

'''
[Card(rank='Q', suit='clubs'), Card(rank='10', suit='spades'), Card(rank='6', suit='spades'), Card(rank='K', suit='diamonds'), Card(rank='Q', suit='spades')]
'''

