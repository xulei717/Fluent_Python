# -*- coding:utf-8 -*-
# @time   : 2019-12-31 10:13
# @author : xulei
# @project: Fluent_Python

class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


if __name__ == '__main__':
    import weakref

    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese
    print(list(stock.items()))
    del catalog
    print(list(stock.items()))
    del cheese
    print(list(stock.items()))
    print()
    '''
    [('Red Leicester', Cheese('Red Leicester')), ('Tilsit', Cheese('Tilsit')), ('Brie', Cheese('Brie')), ('Parmesan', Cheese('Parmesan'))]
    [('Parmesan', Cheese('Parmesan'))]
    []
    '''
    stock = weakref.WeakKeyDictionary()
    stock[Cheese('testValue')] = 'testValue'
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese] = cheese.kind
    print(list(stock.items()))
    del catalog
    print(list(stock.items()))
    del cheese
    print(list(stock.items()))
    print()
    '''
    [(Cheese('Red Leicester'), 'Red Leicester'), (Cheese('Tilsit'), 'Tilsit'), (Cheese('Brie'), 'Brie'), (Cheese('Parmesan'), 'Parmesan')]
    [(Cheese('Parmesan'), 'Parmesan')]
    [] 
    '''
    stock = weakref.WeakKeyDictionary()
    stock[Cheese('testValue')] = 'testValue'
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese] = cheese
    print(list(stock.values()))
    print(list(stock.keys()))
    del catalog
    print(list(stock.values()))
    print(list(stock.keys()))
    del cheese
    print(list(stock.values()))
    print(list(stock.keys()))
    print()
    '''
    [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    '''
    stock = weakref.WeakKeyDictionary()
    stock[Cheese('testValue')] = 'testValue'
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese] = cheese.kind
    print(list(stock.keys()))
    del catalog
    print(list(stock.keys()))
    del cheese
    print(list(stock.keys()))
    print()
    '''
    [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    [Cheese('Parmesan')]
    []
    '''
    stock = weakref.WeakKeyDictionary()
    stock[Cheese('testValue')] = 'testValue'
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese
    print(list(stock.keys()))
    del catalog
    print(list(stock.keys()))
    del cheese
    print(list(stock.keys()))
    print()
    '''
    TypeError: cannot create weak reference to 'str' object
    '''