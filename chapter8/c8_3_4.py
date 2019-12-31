# -*- coding:utf-8 -*-
# @time   : 2019-12-30 13:34
# @author : xulei
# @project: Fluent_Python


charles = {'name': 'charles l. dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(lewis), id(charles))
lewis['balance'] = 950
print(charles)
print()
'''
True
140306629859296 140306629859296
{'name': 'charles l. dodgson', 'born': 1832, 'balance': 950}
'''

alex = {'name': 'charles l. dodgson', 'born': 1832, 'balance': 950}
print(alex == charles)
print(alex is charles)
'''
True
False
'''
