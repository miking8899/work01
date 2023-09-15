# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt  
  
day = ['Monday','Tuesday','Wednesday','Thursday','Friday']  
increase_number = [100,150,180,80,130]  
plt.bar(range(len(day)), increase_number,width=0.8,bottom=None, color='red',tick_label=day)
# plt.bar(range(len(day)), increase_number,width=0.8, color='red',tick_label=day)
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.xlabel('日期')
plt.ylabel('股票上漲個數')
plt.title('股價上漲個數的柱狀圖')  
plt.show()