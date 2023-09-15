# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
# 舉出平面上的許多點
points = np.r_[[[-1,1],[1.5,1.5],[1.8,0.2],[0.8,0.7],[2.2,2.8],[2.5,3.5],[4,2]]]
# 按0和1標示成兩類別
typeName = [0,0,0,0,1,1,1]

# 建立模型
svmTool = svm.SVC(kernel='linear')
svmTool.fit(points,typeName)    # 傳導入參數數

# 確立分類別的直線
sample = svmTool.coef_[0]       # 系數
slope = -sample[0]/sample[1]    # 斜率
lineX = np.arange(-2,5,1)       # 取得-2到5，間距是1的許多資料
lineY = slope*lineX-(svmTool.intercept_[0])/sample[1]
# 畫出劃分直線
plt.plot(lineX,lineY,color='blue',label='Classified Line')
plt.legend(loc='best')          # 繪制圖例
plt.scatter(points[:,0],points[:,1],c='R')
plt.show()