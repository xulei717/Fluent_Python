### chapter9 符合Python风格的对象

**1.classmethod：类方法，用classmethod装饰器修饰。**
* 类方法的第一个参数cls，是类本身，而不是实例。
* 类方法最常见的作用是定义备选构造方法。

**2.format()函数使用格式规范微语言。**
* 格式规范微语言为一些内置类型提供了专用的表示代码。
* b表示二进制，x表示十六进制的int类型，f表示小数形式的float类型，%表示百分数形式。
* 格式规范微语言可扩展。

**3.str.format()方法使用{:}替换字段表示法（包含转换标志!s,!r和!a）**
* 转换标志：跟在叹号 ! 后面的单个字符。当前支持的字符包括r(repr)、s(str)和a(ascii)
* 式说明符：跟在冒号 : 后面的表达式。可指定格式类型(如字符串、浮点数或十六进制数）字段宽度和数的精
度如何显示符号和千位分隔符，以及各种对齐和填充方式。
```python
print("{pi!s} {pi!r} {pi!a}".format(pi = "π"))
# π 'π' '\u03c0'
a = "Hello,{w:s},{y:d},{y:f},{y:.2f},{y:b},{y:%}".format(w="world", y=2019)
# Hello,world,2019,2019.000000,2019.00,11111100011,201900.000000%
```

**4.Python使用一个下划线前缀编写‘受保护’的属性**、
* Python解释器不会对使用单个下划线的属性名做特殊处理
* 但是，Python程序员不会在类外部访问这种属性。

**5.私有属性：属性名前面有两个下划线，尾部没有或最多有一个下划线命名。**
* 名称改写：Python会把私有属性名存入实例的__dict__属性里，而且会在前面加上一个下划线和类名。
* Dog类中的__mood属性，在__dict__属性中会变成_Dog__mood。

**6.类属性可用于为实例属性提供默认值。**
* 如果为不存在的实例属性赋值，会新建实例属性。
* 为实例属性赋值，同名类属性不受影响。
* 自此，实例读取的是实例属性，把同名类属性遮盖了。

**7.特性：通过对属性的读值方法和设值方法增加控制，实现特性，就是属性只可读，在外部不可修改。**
* 在Python中，可以先使用公开属性，然后等需要的时候再变成特性。
* @property装饰器把读值方法标志为特性。

