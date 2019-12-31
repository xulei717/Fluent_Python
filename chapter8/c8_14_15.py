# -*- coding:utf-8 -*-
# @time   : 2019-12-30 14:24
# @author : xulei
# @project: Fluent_Python


class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class TwilightBus1:
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
    basketball_team = ['alice', 'bill', 'claire', 'david']
    bus = TwilightBus(basketball_team)
    bus.drop('alice')
    print(basketball_team)
    print(id(basketball_team), id(bus.passengers))
    print()
    '''
    ['bill', 'claire', 'david']
    140170941687944 140170941687944
    '''
    bus1 = TwilightBus1(basketball_team)
    bus1.drop('bill')
    print(basketball_team)
    print(id(basketball_team), id(bus1.passengers))
    '''
    ['bill', 'claire', 'david']
    140437708790536 140437708903176
    '''