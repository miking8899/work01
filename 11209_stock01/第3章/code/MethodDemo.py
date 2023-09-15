# !/usr/bin/env python
# coding=utf-8
class CalculateTool:
    __PI = 3.14
    @staticmethod
    def add(x,y):
        __result = x+y
        print(x + y) 
    @classmethod
    def calCircle(self,r):
        print(self.__PI*r*r)
CalculateTool.add(23, 22) 		# 輸出45
CalculateTool.calCircle(1) 	    # 輸出3.14  
# 不建議透過物件存取靜態方法和類別方法
tool = CalculateTool()
tool.add(23, 22)
tool.calCircle(1)