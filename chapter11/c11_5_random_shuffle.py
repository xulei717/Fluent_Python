# -*- coding:utf-8 -*-
# @time   : 2019-12-11 16:32
# @author : xulei
# @project: Fluent_Python

from random import shuffle
from chapter11.c11_4_FrenchDeck import FrenchDeck


deck = FrenchDeck()
shuffle(deck)

'''
TypeError: 'FrenchDeck' object does not support item assignment
'FrenchDeck'对象不支持为元素赋值
'''