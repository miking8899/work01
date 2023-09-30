#創建新的類或實例屬性: 創建一個擁有一些額外功能的實例屬性類型，如類型檢查。

描述器 是一個實現三個核心屬性訪問操作的類 (封裝功能)

__get__(self, instance, cls)
__set__(self, instance, value)
__delete__(self, instance)
使用描述器時，需將這個描述器的實例作為類屬性

描述器可實現大部分 Python 類特性中的底層魔法，包括 @classmethod, @staticmethod, @property
# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
p.x # Calls Point.x.__get__(p,Point)
# 2
p.y = 5 # Calls Point.y.__set__(p, 5)
p.x = 2.3 # Calls Point.x.__set__(p, 2.3)
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
#     File "descrip.py", line 12, in __set__
#         raise TypeError('Expected an int')
# TypeError: Expected an int

#類裝飾器描述器程式碼 (template)

# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
        
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value
        
    def __delete__(self, instance):
        del instance.__dict__[self.name]

# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
只想定義類中單個屬性訪問的話就不用去寫描述器了，使用property 會更加恰當。當程序中有很多重複代碼的時候描述器就很有用了。

使用延遲計算屬性: x

簡化數據結構的初始化: 要寫很多僅用作數據結構的類，不想寫一堆煩人的 __init__() 函數

支持位置參數
import math

class Structure1:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# Example class definitions
class Stock(Structure1):
    _fields = ['name', 'shares', 'price']

class Point(Structure1):
    _fields = ['x', 'y']

class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


s = Stock('ACME', 50, 91.1)
p = Point(2, 3)
c = Circle(4.5)
s2 = Stock('ACME', 50)
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
#     File "structure.py", line 6, in __init__
#         raise TypeError('Expected {} arguments'.format(len(self._fields)))
# TypeError: Expected 3 arguments
支持關鍵字參數
class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
# Example use
if __name__ == '__main__':
    class Stock(Structure2):
        _fields = ['name', 'shares', 'price']

    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, price=91.1)
    s3 = Stock('ACME', shares=50, price=91.1)
    # s3 = Stock('ACME', shares=50, price=91.1, aa=1)
將不在 _fields 中的名稱加入到屬性中去 (template)
class Structure3:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))

# Example use
if __name__ == '__main__':
    class Stock(Structure3):
        _fields = ['name', 'shares', 'price']

    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, 91.1, date='8/2/2012')