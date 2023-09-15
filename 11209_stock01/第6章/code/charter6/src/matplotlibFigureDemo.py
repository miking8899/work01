# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
# 定義資料
x = np.array([1,2,3,4,5])
# 第一個figure
plt.figure(num=1, figsize=(3, 3),facecolor='yellow')
plt.plot(x, x*x)
# 第二個figure
plt.figure(num=2, figsize=(4, 4),edgecolor='red') 
plt.plot(x, x*x*x)
plt.show()