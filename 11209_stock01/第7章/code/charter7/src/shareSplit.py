﻿# !/usr/bin/env python
# coding=utf-8
import numpy as np
x = np.arange(0,5,1)
y = x[2:4]
y[0]=10
print(y)		# 輸出[10  3]
print(x)		# 輸出[ 0  1 10  3  4]
c=x.copy()
c[0]=20
print(x)		# 輸出依然是[ 0  1 10  3  4]，沒改變

