# -*- coding:utf-8 -*-
# @time   : 2019-12-16 14:55
# @author : xulei
# @project: Fluent_Python

import doctest

from chapter11.c11_9_tombola import Tombola

# 要测试的模块
import chapter11.c11_12_bingo, chapter11.c11_13_lotto, chapter11.c11_14_tombolist

"""
Tombola子类的测试运行程序
"""

TEST_FILE = 'c11_16_tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'


def main(argv):
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()  # 返回的列表是内存中存在的直接子代。即便源码中用不到想测试的模块，也要将其导入，因为要把那些类载入内存
    virtual_subclasses = list(Tombola._abc_registry)  # _abc_registry:WeakSet对象

    for cls in real_subclasses + virtual_subclasses:  # 迭代找到的各个子类
        test(cls, verbose)


def test(cls, verbose=False):

    res = doctest.testfile(TEST_FILE,
                           globs={'ConcreteTombola': cls},  # 把cls参数（要测试的类）绑定到全局命名空间里的ConcreteTombola名称上，供doctest使用
                           verbose=verbose,
                           optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))


if __name__ == '__main__':
    import sys
    main(sys.argv)

'''
BingoCage         0 tests,  0 failed - OK
LotteryBlower     0 tests,  0 failed - OK
TomboList         0 tests,  0 failed - OK
'''
'''
/usr/bin/python3 /home/xl/CodeStore/Fluent_Python/chapter11/c11_15_tombola_runner.py
**********************************************************************
File "/home/xl/CodeStore/Fluent_Python/chapter11/c11_16_tombola_tests.rst", line 25, in c11_16_tombola_tests.rst
Failed example:
    globe.load(balls)
Expected:
    False
Got nothing
**********************************************************************
1 items had failures:
   6 of  24 in c11_16_tombola_tests.rst
***Test Failed*** 6 failures.
BingoCage        24 tests,  6 failed - FAIL
**********************************************************************
File "/home/xl/CodeStore/Fluent_Python/chapter11/c11_16_tombola_tests.rst", line 25, in c11_16_tombola_tests.rst
Failed example:
    globe.load(balls)
Expected:
    False
Got nothing
**********************************************************************
1 items had failures:
   6 of  24 in c11_16_tombola_tests.rst
***Test Failed*** 6 failures.
LotteryBlower    24 tests,  6 failed - FAIL
**********************************************************************
File "/home/xl/CodeStore/Fluent_Python/chapter11/c11_16_tombola_tests.rst", line 19, in c11_16_tombola_tests.rst
Failed example:
    picks.append(globe.pick())
Exception raised:
    Traceback (most recent call last):
      File "/usr/local/python3.6/lib/python3.6/doctest.py", line 1330, in __run
        compileflags, 1), test.globs)
      File "<doctest c11_16_tombola_tests.rst[5]>", line 1, in <module>
        picks.append(globe.pick())
      File "/home/xl/CodeStore/Fluent_Python/chapter11/c11_14_tombolist.py", line 21, in pick
        position = randrange(self)
      File "/usr/local/python3.6/lib/python3.6/random.py", line 183, in randrange
        istart = _int(start)
    TypeError: int() argument must be a string, a bytes-like object or a number, not 'TomboList'
**********************************************************************
1 items had failures:
  11 of  24 in c11_16_tombola_tests.rst
***Test Failed*** 11 failures.
TomboList        24 tests, 11 failed - FAIL

Process finished with exit code 0

'''
'''
BingoCage        23 tests,  0 failed - OK
LotteryBlower    23 tests,  0 failed - OK
TomboList        23 tests,  0 failed - OK
'''
