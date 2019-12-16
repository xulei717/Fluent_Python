# -*- coding:utf-8 -*-
# @time   : 2019-12-10 17:30
# @author : xulei
# @project: Fluent_Python


class Vector2d:

    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))


if __name__ == '__main__':

    v = Vector2d(1, 2)
    print(v.x, v.y, v.typecode)  # 1.0 2.0 d
    print([x for x in v])  # [1.0, 2.0]

    v.x = 100
    print([x for x in v])  # [100, 2.0]

