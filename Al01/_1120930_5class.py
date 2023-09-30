定義接口或抽象基類: 想定義一個接口或抽像類，並且通過執行類型檢查來確保子類實現了某些特定的方法。

抽像類不能直接被實例化
抽像類的目的是讓別的類繼承它並實現特定的抽象方法 (多態)
元類 (walk, attack, attacked, die)
神獸
士兵
英雄
from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

a = IStream() # TypeError: Can't instantiate abstract class
                # IStream with abstract methods read, write

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass
實現數據模型的類型約束 x

實現自定義容器: 實現自定義類來模擬容器類的功能，如列表和字典，但是你不確定到底要實現哪些方法。collections 定義很多抽象基類 (collections.Iterable, collections.Sequence)，自定義容器類時候它們非常有用

繼承
實現抽象方法
class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 1, 3])
print(list(items))
print(items[0], items[-1])
items.add(2)
print(list(items))
屬性的代理訪問: 將某個實例的屬性訪問代理到內部另一個實例中去，作為繼承的一個替代方法或者實現代理模式。


簡單代理
class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)

    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()

    def bar(self):
        pass
大量的方法需要代理
class B2:
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        """the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found"""
        return getattr(self._a, name)
    
b = B()
b.bar() # Calls B.bar() (exists on B)
b.spam(42) # Calls B.__getattr__('spam') and delegates to A.spam
__getattr__ 方法是在訪問屬性或方法不存在時才被調用。

代理模式
# A proxy class that wraps around another object, but
# exposes its public attributes
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)

            
class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)

# Create an instance
s = Spam(2)
# Create a proxy around it
p = Proxy(s)
# Access the proxy
print(p.x)  # Outputs 2
p.bar(3)  # Outputs "Spam.bar: 2 3"
p.x = 37  # Changes s.x to 37
通過自定義屬性訪問方法，你可以用不同方式自定義代理類行為。

繼承 (is a): 人 --> 黃種人，白種人，黑人
組合 (has a): 人 --> 手，腳，頭，…
代理: 總公司 --> 代理商
繼承
class A:
    def spam(self, x):
        print('A.spam', x)
        
    def foo(self):
        print('A.foo')

class B:
    def __init__(self):
        self._a = A()
        
    def spam(self, x):
        print('B.spam', x)
        self._a.spam(x)
        
    def bar(self):
        print('B.bar')
        
    def __getattr__(self, name):
        return getattr(self._a, name)
注意:

__setattr__() 和 __delattr__() 需要額外的魔法來區分代理實例和被代理實例 _obj 的屬性。一個通常的約定是只代理那些不以下劃線 _ 開頭的屬性
__getattr__() 對於大部分以雙下劃線 __ 開始和結尾的屬性並不適用