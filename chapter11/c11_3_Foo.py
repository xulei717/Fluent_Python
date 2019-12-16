# -*- coding:utf-8 -*-
# @time   : 2019-12-11 16:15
# @author : xulei
# @project: Fluent_Python


class Foo:
    def __getitem__(self, item):
        return range(0, 30, 10)[item]


if __name__ == '__main__':

    f = Foo()   # 可迭代对象
    print(f[1])
    for i in f:
        print(i)

    print(20 in f)
    print(15 in f)

'''
10
0
10
20
True
False
'''