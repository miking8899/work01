# !/usr/bin/env python
# coding=utf-8
import numpy as np 	# 匯入numpy庫，有個別名np
arr = np.array(np.arange(4)) # 建立一個序列
print(arr) 			# 輸出 [0 1 2 3]
print(np.eye(2)) 	# 建立一個維度是2的對角矩陣，輸出如下
# [[1. 0.]
# [0. 1.]]