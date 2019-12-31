# -*- coding:utf-8 -*-
# @time   : 2019-12-20 17:15
# @author : xulei
# @project: Fluent_Python


class MySeq:
    def __getitem__(self, index):
        return index


if __name__ == '__main__':
    s = MySeq()
    print(s[1])
    print(s[1:4])
    print(s[1:4:2])
    print(s[1:4:2, 9])
    print(s[1:4:2, 7:9])
    '''
    1
    slice(1, 4, None)
    slice(1, 4, 2)
    (slice(1, 4, 2), 9)
    (slice(1, 4, 2), slice(7, 9, None))
    '''
    print()
    print(slice)
    print(dir(slice))
    print(help(slice.indices))
    print(slice(None, 10, 2).indices(5))  # 长度为5的序列的[:10:2]相当于[0:5:2]
    print(slice(-3, None, None).indices(5)) # 长度为5的序列的[-3:]相当于[2:5:1]
    '''
    <class 'slice'>
    ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
     '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', 
     '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'indices', 'start', 
     'step', 'stop']
    Help on method_descriptor:

    indices(...)
        S.indices(len) -> (start, stop, stride)
        
        Assuming a sequence of length len, calculate the start and stop
        indices, and the stride length of the extended slice described by
        S. Out of bounds indices are clipped in a manner consistent with the
        handling of normal slices.
    
    None
    
    (0, 5, 2)
    (2, 5, 1)
    '''