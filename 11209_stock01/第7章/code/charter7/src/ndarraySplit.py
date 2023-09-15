# !/usr/bin/env python
# coding=utf-8
import numpy as np
arr1 = np.arange(0,11,1)
# 輸出[ 0  1  2  3  4  5  6  7  8  9 10]
print(arr1)
arrSplit1 = arr1[2:5]
# 輸出[2 3 4]
print(arrSplit1)
# 輸出[2 3 4 5 6 7 8 9]，不包括10
print(arr1[2:-1])		# -1表示最右邊的元素
# 輸出[ 2  3  4  5  6  7  8  9 10]
print(arr1[2:])		# 表示從2號索引開始到最後，包括10
# 輸出[0 1 2 3 4]
print(arr1[:5])		# 表示從0號索引開始到5號索引
# 輸出[2 3 4 5 6 7 8]
print(arr1[2:-2])		# -2表示右邊開始第2個元素
# 輸出[0 1 2 3 4 5 6 7]
print(arr1[:-3])		# -3表示右邊開始第3個元素
# 針對多維陣列的切片
arr2 = np.array([[1, 2, 3],[4, 5, 6]])
# a輸出[[2 3]
#       [5 6]]
print(arr2[[0,1],1:])