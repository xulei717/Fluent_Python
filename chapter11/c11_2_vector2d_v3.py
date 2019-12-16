# -*- coding:utf-8 -*-
# @time   : 2019-12-10 17:30
# @author : xulei
# @project: Fluent_Python

"""
@property装饰器：把方法变成属性，可以调用获得属性值
@x.setter装饰器：可以给私有属性进行赋值，没有这个方法则认为属性是只可读的不可写
"""


class Vector2d:
    typeCode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, v):
        if isinstance(v, int):
            self.__x = v
        else:
            print("x赋值的值类型不对，应该是int型！！！")

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))


if __name__ == '__main__':

    v = Vector2d(1, 2)
    print(v, type(v))
    print(v.x, v.y, v.typeCode)
    print([x for x in v])

    v.x = 3
    print(v.x)
    print([x for x in v])

    v.x = '2'

'''
<__main__.Vector2d object at 0x7fc264dec438> <class '__main__.Vector2d'>
1.0 2.0 d 
[1.0, 2.0]
3
[3, 2.0]
x赋值的值类型不对，应该是int型！！！
'''