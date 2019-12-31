# -*- coding:utf-8 -*-
# @time   : 2019-12-18 15:30
# @author : xulei
# @project: Fluent_Python

"""
1.classmethod：作用是操作类，比如定义备选构造函数，类方法的第一个参数是类身边，而不是实例。
2.staticmethod：第一个参数不是特殊的值。静态方法就是普通的函数，只是碰巧在类的定义体中，而不是在模块层定义。
"""


class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


if __name__ == '__main__':
    print(Demo.klassmeth())
    print(Demo.klassmeth('spam'))
    print(Demo.klassmeth('spam', 'dsf'))
    print(Demo.statmeth())
    print(Demo.statmeth('spam'))
    print(Demo.statmeth('spam', 'dsf'))
'''
(<class '__main__.Demo'>,)
(<class '__main__.Demo'>, 'spam')
(<class '__main__.Demo'>, 'spam', 'dsf')
()
('spam',)
('spam', 'dsf')
'''