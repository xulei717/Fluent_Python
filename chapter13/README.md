### chapter13 正确重载运算符

**1.对整数按位取反，定义为 ~x == -(x+1)**

**2.支持一元运算符很简单，只需要实现相应的特殊方法。**
* 这些特殊方法只有一个参数，self。
* 要遵守运算符的一个基本规则：始终返回一个新对象。
* 不能修改self，要创建并返回合适类型的新实例。

**3.实现一元运算符和中缀运算符特殊方法一定不能修改操作数。使用这些运算符的表达式期待结果是新对象。只有增量赋值表达式可能会修改第一个操作数self。**

**4.如果中缀运算符方法抛出异常，就终止了运算符分派机制。**
* 对TypeError来说，通常最好将其捕获，然后返回NotImplemented。
* 这样，解释器会尝试调用反向运算符方法，如果操作数是不同类型，对调之后，反向运算符方法可能会正确计算。

**5.从Python3.5起，@记号可以用作中缀点积运算符。**

**6.生成器表达式在最后时刻才会计算，而不是在源码中定义它的位置计算。**

