# !/usr/bin/env python
# coding=utf-8
import numpy as np

arr1 = np.arange(0,1,0.2)
# 輸出[0.  0.2 0.4 0.6 0.8]
print(arr1)
# 輸出<class 'numpy.ndarray'>
print(type(arr1))
print(arr1.ndim)    # 傳回arr1的維數，是1
# 輸出[1 2 3 4]
print(np.array(range(1,5)))
arr2=np.array([[1,2,3],[4,5,6]])    # 二維陣列
print(arr2.ndim)    # 傳回2
print(arr2.size)    # 總長度，傳回6
print(arr2.dtype)   # 型態，傳回int32
# 形狀，傳回(2, 3)，表示二維陣列，每個維度長度是3
print(arr2.shape) 
arr3=np.array([1,3,5])
print(arr3.mean())  # 計算平均數，傳回3
print(arr3.sum())   # 計算和，傳回9
# 計算所有行的平均數，傳回[2. 5.]
print(arr2.mean(axis=1)) 
# 計算所有列的平均數，傳回[2.5 3.5 4.5]
print(arr2.mean(axis=0))