# -*- coding:utf-8 -*-
# @time   : 2019-12-11 18:06
# @author : xulei
# @project: Fluent_Python


field_names = 'sd dsf, sdf,sdd'

try:
    field_names = field_names.replace(',', ' ').split()
except AttributeError:
    pass
field_names = tuple(field_names)
print(field_names)  # ('sd', 'dsf', 'sdf', 'sdd')
