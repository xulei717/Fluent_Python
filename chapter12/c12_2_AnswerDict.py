# -*- coding:utf-8 -*-
# @time   : 2019-12-16 17:15
# @author : xulei
# @project: Fluent_Python

"""
1.dict.update方法会忽略AnswerDict.__getitem__方法
"""


class AnswerDict(dict):
    def __getitem__(self, key):
        return 42


if __name__ == '__main__':
    ad = AnswerDict(a='foo')
    print(ad['a'])
    d = {}
    d.update(ad)
    print(d['a'])
    print(d)
'''
42
foo
{'a': 'foo'}
'''