# !/usr/bin/env python
# coding=utf-8
# 定義類別
class Stock:
    def __init__(self,stockCode):
        print("in __init__")
        self.stockCode = stockCode
    # 回收類別的時候被觸發 
    def __del__(self):
        print("In __del__")
    def __str__(self):
        print("in __str__")
        return "stockCode is: "+self.stockCode
    def __repr__(self):        
        return "stockCode is: "+self.stockCode
    def __setattr__(self, name, value): 
        print("in __setattr__")
        self.__dict__[name] = value  # 給類別中的屬性名分配值 
    def __getattr__(self, key):
        print("in __setattr__")  
        if key == "stockCode":
            return self.stockCode
        else:
            print("Class has no attribute '%s'" % key)
# 起始化類別，並呼叫類別裡的方法
myStock = Stock("600128")       # 觸發__init__和 __setattr__方法   
print(myStock)                  # 觸發__str__和__repr__方法
myStock.stockCode = "600020"    # 觸發__setattr__方法