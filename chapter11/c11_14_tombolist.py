# -*- coding:utf-8 -*-
# @time   : 2019-12-16 14:37
# @author : xulei
# @project: Fluent_Python

from random import randrange

from chapter11.c11_9_tombola import Tombola

"""
1.注册虚拟子类的方式是在抽象基类上调用register方法，issubclass和isinstance等函数都能识别，但是注册的类不会从抽象基类中继承任何方法或属性。
2.虚拟子类不会继承注册的抽象基类，而且任何适合都不会检查它是否符合抽象基类的接口，即便在实例化时也不会检查。为了避免运行时错误，虚拟子类要实现所需的全部方法。
"""


@Tombola.register  # 把TomboList注册为Tombola的虚拟子类
class TomboList(list):

    def pick(self):
        if self:  # 从list继承__bool__方法，列表不为空时返回True
            position = randrange(len(self))
            return self.pop(position)  # 调用继承自list的self.pop方法，传入一个随机的元素索引
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # TomboList.load与list.extend一样

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(TomboList)  # Python 3.3或之前的版本，不能用装饰器，必须使用标准的调用语法。


if __name__ == '__main__':
    print(issubclass(TomboList, Tombola))
    t = TomboList(range(100))
    print(t)
    print(isinstance(t, Tombola))
    print(TomboList.__mro__)  # 按顺序列出类及其超类

'''
True
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
True
(<class '__main__.TomboList'>, <class 'list'>, <class 'object'>)
'''