# -*- coding:utf-8 -*-
# @time   : 2019-12-30 14:24
# @author : xulei
# @project: Fluent_Python


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    import copy

    bus1 = Bus(['alice', 'bill', 'claire', 'david'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))
    bus1.drop('bill')
    print(id(bus1), id(bus2), id(bus3))
    print(bus2.passengers)
    print(bus3.passengers)
    '''
    140435265214280 140435265214672 140435265215960
    140435265214280 140435265214672 140435265215960
    ['alice', 'claire', 'david']
    ['alice', 'bill', 'claire', 'david']
    '''