# -*- coding:utf-8 -*-
# @time   : 2019-12-18 14:50
# @author : xulei
# @project: Fluent_Python

from array import array

"""
1.内存视图其实是泛化和去数学化的numpy数组，它让你在不需要复制内容的前提下，
在数据结构之间共享内存，其中数据结构可以是任何形式的，比如PIL图片，SQLite数据库，numpy的数组等。
这个功能在处理大型数据集合的时候非常重要。
memoryview.cast()方法的概念跟数组模块类似，能用不同的方式读写同一块内存，而且内容字节不会随意移动。
2.利用memoryview来操作二进制序列
"""


numbers = array('h', [-2, -1, 0, 1, 2])  # type 'h': signed short

mem_short = memoryview(numbers)
print(len(mem_short))
print(mem_short[0])
print(mem_short.tolist())
print(len(numbers))
print(numbers[0])
print(numbers)
'''
5
-2
[-2, -1, 0, 1, 2]
5
-2
array('h', [-2, -1, 0, 1, 2])
'''
mem_octets = mem_short.cast('B')  # type 'B': unsigned char
print(len(mem_octets), mem_octets.tolist())
mem_octets[5] = 4
print(len(numbers), numbers)
'''
10 [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
5 array('h', [-2, -1, 1024, 1, 2])
'''