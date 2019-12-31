# -*- coding:utf-8 -*-
# @time   : 2019-12-18 15:43
# @author : xulei
# @project: Fluent_Python

"""
1.format(my_obj, format_spec)函数：使用格式规范微语言
2.str.format()函数：使用格式字符串句法，{:}代换字段表示法（包含转换标志!s、!r和!a）
"""
"""
3.格式规范微语言：https://docs.python.org/3/library/string.html#formatspec
    3.1为一些内置类型提供了专用的表示代码。比如，b和x分别表示二进制和十六进制的int类型，f表示小数形式的float类型，而%表示百分数形式；
    3.2是可扩展的，因为各个类可以自行决定如何解释format_spec参数。
"""

brl = 1/2.43
print(brl)
print(format(brl, '0.4f'))  # '0.4f'是格式说明符
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))
'''
0.4115226337448559
0.4115
1 BRL = 0.41 USD
'''
print(format(42, 'b'))
print(format(2/3, '.1%'))
'''
101010
66.7%
'''
from datetime import datetime
now = datetime.now()
print(format(now, '%H:%M:%S'))
print("it's now {:%I:%M %p}".format(now))
'''
15:52:28
it's now 03:52 PM
'''
coord = (3, 5)
print('{1}, {0}'.format(*coord))
print('{0[1]}, {0[0]}'.format(coord))
'''
5, 3
5, 3
'''
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))
print('repr() shows quotes: {!r}; str() does: {!s}'.format('test1', 'test2'))
'''
repr() shows quotes: 'test1'; str() doesn't: test2
repr() shows quotes: 'test1'; str() does: test2
'''
print('{:*<30}'.format('left aligned'))
print('{:*>30}'.format('right aligned'))
print('{:*^30}'.format('centered'))  # use '*' as a fill char
'''
left aligned******************
*****************right aligned
***********centered***********
'''
print('{:+f}; {:+f}'.format(3.14, -3.14))
print('{:.3f}; {:.3f}'.format(3.14, -3.14))
print('{:-f}; {:-f}'.format(3.14, -3.14))
'''
+3.140000; -3.140000
3.140; -3.140
3.140000; -3.140000
'''
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print("int: {0:#d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
'''
int: 42;  hex: 2a;  oct: 52;  bin: 101010
int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010
'''
print('{:,}'.format(1234567890))
print('{:_}'.format(1234567890))
'''
1,234,567,890
1_234_567_890
'''
for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))
'''
left<<<<<<<<<<<<
^^^^^center^^^^^
>>>>>>>>>>>right
'''
print('{:02X}{:02X}{:02X}{:02X}'.format(*[192, 168, 0, 1]))
'''
C0A80001
'''
print(int('C0A80001', 16))
'''
3232235521
'''
for num in range(5,12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=5), end=' ')
    print()
'''
    5     5     5   101 
    6     6     6   110 
    7     7     7   111 
    8     8    10  1000 
    9     9    11  1001 
   10     A    12  1010 
   11     B    13  1011 
'''
from string import Template
s = Template('$who likes $what')
print(s.substitute(who='tim', what='kung pao'))
d = dict(who='tim')
print(Template('$who likes $what').safe_substitute(d))
print(Template('$who likes pao').substitute(d))
# print(Template('$who likes $100').substitute(d))
print(Template('$who likes $what').substitute(d))
'''
tim likes kung pao
tim likes $what
tim likes pao
ValueError: Invalid placeholder in string: line 1, col 12
KeyError: 'what'
'''
