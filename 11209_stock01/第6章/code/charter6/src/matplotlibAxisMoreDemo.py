# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

xmajorLocator   = MultipleLocator(5)            # 將x軸主刻度設定為5的倍數
xmajorFormatter = FormatStrFormatter('%1.1f')   # 設定x軸標簽的格式
xminorLocator   = MultipleLocator(1)            # 將x軸次刻度設定為1的倍數
ymajorLocator   = MultipleLocator(0.5)          # 將y軸主刻度設定為0.5的倍數
ymajorFormatter = FormatStrFormatter('%1.2f')   # 設定y軸標簽的格式
yminorLocator   = MultipleLocator(0.1)          # 將y軸次刻度設定為0.1的倍數
 
x = np.arange(0, 21, 0.1)
ax = plt.subplot(111)
# 設定主刻度標簽的位置，標籤文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

# 顯示次刻度標簽的位置，沒有標籤文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
y = np.sin(x)       # 繪圖，圖形為y=sinx
plt.plot(x,y)
plt.show()