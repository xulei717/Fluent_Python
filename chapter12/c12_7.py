# -*- coding:utf-8 -*-
# @time   : 2019-12-16 18:17
# @author : xulei
# @project: Fluent_Python

from chapter12.c12_4_diamond import D

d = D()
d.pingpong()
'''
ping: <chapter12.c12_4_diamond.D object at 0x7ff4359fcc88>
post-ping: <chapter12.c12_4_diamond.D object at 0x7ff4359fcc88>
ping: <chapter12.c12_4_diamond.D object at 0x7ff4359fcc88>
pong: <chapter12.c12_4_diamond.D object at 0x7ff4359fcc88>
pong: <chapter12.c12_4_diamond.D object at 0x7ff4359fcc88>
PONG: <chapter12.c12_4_diamond.D object at 0x7ff4359fcc88>
'''