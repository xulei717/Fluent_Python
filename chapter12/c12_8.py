# -*- coding:utf-8 -*-
# @time   : 2019-12-16 18:20
# @author : xulei
# @project: Fluent_Python


print(bool.__mro__)


def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))


print_mro(bool)


from chapter11.c11_8_frenchdeck2 import FrenchDeck2
print_mro(FrenchDeck2)


import numbers
print_mro(numbers.Integral)


import io
print_mro(io.BytesIO)
print_mro(io.TextIOWrapper)

'''
(<class 'bool'>, <class 'int'>, <class 'object'>)
bool, int, object
FrenchDeck2, MutableSequence, Sequence, Reversible, Collection, Sized, Iterable, Container, object
Integral, Rational, Real, Complex, Number, object
BytesIO, _BufferedIOBase, _IOBase, object
TextIOWrapper, _TextIOBase, _IOBase, object
'''
