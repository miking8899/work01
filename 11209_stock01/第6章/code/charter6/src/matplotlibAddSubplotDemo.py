# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10) 
# 新增figure物件
fig=plt.figure()
# 子圖1
ax1=fig.add_subplot(3,3,1)
ax1.plot(x, x)
# 子圖2
ax3=fig.add_subplot(3,3,5)
ax3.plot(x, x * x)
# 子圖4
ax4=fig.add_subplot(3,3,9)
ax4.plot(x, 1/x)
plt.show()