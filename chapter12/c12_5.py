# -*- coding:utf-8 -*-
# @time   : 2019-12-16 17:59
# @author : xulei
# @project: Fluent_Python

from chapter12.c12_4_diamond import *


d = D()
d.pong()
C.pong(d)  # 直接在类上调用实例方法时，必须显示传入参数

'''
pong: <chapter12.c12_4_diamond.D object at 0x7fc36d9bed30>
PONG: <chapter12.c12_4_diamond.D object at 0x7fc36d9bed30>
'''