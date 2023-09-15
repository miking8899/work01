# !/usr/bin/env python
# coding=utf-8
import numpy as np
arr1 = np.arange(0,1,0.2)
# 輸出0.4
print(arr1[2])
# 會報出“索引越界”的錯誤
#print(arr1[6])
arr2 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# 傳回[4 5 6]
print(arr2[1])
# 傳回6
print(arr2[1,2])
arr3 = np.arange(5)
bool = np.array([True,False,False,True,True])
# 輸出[0 3 4]
print(arr3[bool])
arr4=arr3[arr3>2]
# 輸出[3 4]
print(arr4)