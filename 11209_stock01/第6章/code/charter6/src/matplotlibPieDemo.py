# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
# 顯示中文字元
plt.rcParams['font.sans-serif']=['SimHei'] 
labels = ['薪水','股票','基金','著書收益','視訊教學收益','其他']
sizes = [23000,2000,2000,1500,2000,800]
explode = (0,0.1,0.1,0.1,0.1,0.1)
colors=['red','blue','green','#ffff00','#ff00ff','#f0f000']
plt.pie(sizes,explode=explode,labels=labels,startangle=45,colors=colors)
plt.title("本月收入情況")
plt.show()