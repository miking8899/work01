# !/usr/bin/env python
# coding=utf-8
class Shape:    # 定義父類別
    _size=0     # 受保護的屬性
    def __init__(self,type,size):              
        self._type = type  
        self._size = size
    def _set_type(self,type):   # 受保護的方法
        self._type=type
    def _get_type(self):        # 受保護的方法
        return self._type
class Circle(Shape):        # 定義子類別
    def set_size(self,size): 
       self._size = size    # 覆蓋了父類別的_size屬性
    def printSize(self): 
       print(self._size)    
class anotherClass:         # 定義不相干的一個類別
    pass                    # 若果是空方法，則需要加個pass，否則會顯示出錯
# 使用子類別
c=Circle("Square",2)
c._set_type("Circle")
print(c._get_type())
c.printSize()
anotherClass._set_type("Circle")  # 會顯示出錯