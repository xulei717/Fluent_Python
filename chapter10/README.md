### chapter10  序列的修改、散列和切片

**1.使用reprlib模块可以生成长度有限的表现形式**

```python
import reprlib
from array import array

print(reprlib.repr(array('d', range(100))))
#  array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
```

**2.__slots__属性可以防止设置新实例属性。**
**__slots__属性只应该用于节省内存，而且仅当内存严重不足时才应该这么做。**

**3.多数时候，如果实现了__getattr__方法，那么也要定义__setattr__方法，以防止对象的行为不一致。**

**4.映射规约：把函数应用到各个元素上，生成一个新序列（映射，map），然后计算聚合值（规约，reduce）**

**5.zip函数生成一个由元组构成的生成器，一旦有一个输入耗尽，zip函数会立即停止生成值，而且不发出警告。**

**6.格式化函数format，用__format__方法实现。**
**浮点数格式代码：'eEfFgGn%'，整数格式代码：'bcdoxXn'，字符串格式代码：'s'**

**7.动态类型语言中的既定协议会自然进化。**
**所谓动态类型是指在运行时检查类型，因为方法签名和变量没有静态类型信息。**

**8.在Python文档中，如果看到‘文件类对象’这样的表述，通常说的就是协议。**
