# -*- coding:utf-8 -*-
# @time   : 2019-12-17 14:54
# @author : xulei
# @project: Fluent_Python

"""
1.算数运算上下文的精度变化可能导致x不等于+x
"""


import decimal

ctx = decimal.getcontext()  # 获取当前全局算术运算的上下文引用
ctx.prec = 18               # 设定算术运算上下文的精度，以设定的最小值为准
one_third = decimal.Decimal('1') / decimal.Decimal('3')
print(one_third)
print(one_third == +one_third)

ctx.prec = 10
print(one_third == +one_third)
print(+one_third)

'''
40 28
0.3333333333333333333333333333333333333333
True
False
0.3333333333333333333333333333
'''
'''
4 8
0.3333
True
True
0.3333
'''
'''
10 18
0.3333333333
True
True
0.3333333333
'''
'''
18 10
0.333333333333333333
True
False
0.3333333333
'''