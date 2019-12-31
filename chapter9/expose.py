# -*- coding:utf-8 -*-
# @time   : 2019-12-20 14:52
# @author : xulei
# @project: Fluent_Python

import chapter9.Confidential

"""
Jython代码
"""

message = chapter9.Confidential('top secret text')
secret_field = chapter9.Confidential.getDeclaredField('secret')
secret_field.setAccessible(True)  # 攻破防线
print('message.secret = ', secret_field.get(message))

'''
$jpython expose.py

'''