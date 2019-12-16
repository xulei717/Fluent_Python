# -*- coding:utf-8 -*-
# @time   : 2019-12-16 13:09
# @author : xulei
# @project: Fluent_Python

import abc

"""
1.抽象基类要继承abc.ABC
2.抽象方法使用@abstractmethod装饰器标记，而且定义体中通常只有文档字符串
3.根据文档字符串，如果没有元素可选，应该抛出LookupError
4.抽象基类中的具体方法只能依赖抽象基类定义的接口，即只能使用抽象基类中的其他具体方法、抽象方法或特性
5.抽象方法可以有实现代码。即使实现了，子类也必须覆盖抽象方法，但是在子类中可以使用super()函数调用抽象方法，为它添加功能
6.与其他方法描述符一起使用时，abstractmethod()应该放在最里面
"""


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回。
        如果实例为空，这个方法应该抛出‘LookupError’。
        """

    def loaded(self):
        """如果至少有一个元素，返回True，否则返回False"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，由当前元素组成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

