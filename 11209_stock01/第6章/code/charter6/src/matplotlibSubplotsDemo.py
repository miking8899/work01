# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 5) 
plt.figure()        # 設定白板
plt.subplot(2,1,1)  # 第一個子圖在2*1的第1個位置
plt.plot(x,x*x)
plt.subplot(2,2,3)  # 第二個子圖在2*2的第3個位置
plt.plot(x,1/x)
plt.subplot(224)    # 第三個子圖在2*2的第4個位置
plt.plot(x,x*x*x)
plt.show()