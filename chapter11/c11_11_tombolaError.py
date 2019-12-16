# -*- coding:utf-8 -*-
# @time   : 2019-12-16 13:56
# @author : xulei
# @project: Fluent_Python

from chapter11.c11_9_tombola import Tombola


class Fake(Tombola):
    def pick(self):
        return 13


if __name__ == '__main__':
    print(Fake)
    f = Fake()

'''
<class '__main__.Fake'>
Traceback (most recent call last):
  File "/home/xl/CodeStore/Fluent_Python/chapter11/c11_11_tombolaError.py", line 16, in <module>
    f = Fake()
TypeError: Can't instantiate abstract class Fake with abstract methods load
'''