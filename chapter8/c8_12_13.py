# -*- coding:utf-8 -*-
# @time   : 2019-12-30 14:24
# @author : xulei
# @project: Fluent_Python


class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    bus1 = HauntedBus(['alice', 'bill'])
    print(bus1.passengers)
    bus1.pick('charlie')
    bus1.drop('alice')
    print(bus1.passengers)
    print()
    '''
    ['alice', 'bill']
    ['bill', 'charlie']
    '''
    bus2 = HauntedBus()
    bus2.pick('carrie')
    print(bus2.passengers)
    print()
    '''
    ['carrie']
    '''
    bus3 = HauntedBus()
    print(bus3.passengers)
    bus3.pick('dave')
    print(bus2.passengers)
    print(bus2.passengers is bus3.passengers)
    print(bus1.passengers)
    print()
    '''
    ['carrie']
    ['carrie', 'dave']
    True
    ['bill', 'charlie']
    '''
    print(dir(HauntedBus.__init__))
    print(HauntedBus.__init__.__defaults__)
    print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)
    '''
    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    (['carrie', 'dave'],)
    True
    '''