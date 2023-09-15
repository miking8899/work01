# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
stockPrice = [10.5, 21.6, 11.7, 20.8, 30.7,17.8, 15.7, 20.9]
group = [10, 20, 30, 40]
plt.hist(stockPrice, group, histtype='bar', rwidth=0.8)
plt.xticks(np.arange(0,50,10))
plt.yticks(np.arange(0,5,1))
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.xlabel('股價分群組')
plt.ylabel('個數')
plt.title('統計股價分群組的直方圖')
plt.show()