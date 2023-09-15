# !/usr/bin/env python
# coding=utf-8
from matplotlib.dates import WeekdayLocator, DayLocator, MONDAY
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import datetime as dt
 
fig = plt.figure()
ax = fig.add_subplot(111)   # 定義圖的位置
startDate = dt.datetime(2019,4,1)
endDate = dt.datetime(2019,4,30)
interval = dt.timedelta(days=1)
dates = mpl.dates.drange(startDate, endDate, interval)
y = np.random.rand(len(dates))*10               # 產生許多個隨機數
ax.plot_date(dates, y, linestyle='-.')          # 設定時間序列
# ax.plot_date(dates, y, linestyle='-.')        # 可以檢視這個型態
dateFmt = mpl.dates.DateFormatter('%Y-%m-%d')   # 時間的顯示格式
# 設定主刻度和次刻度的時間
mondays = WeekdayLocator(MONDAY)
alldays = DayLocator()
ax.xaxis.set_major_formatter(dateFmt)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
fig.autofmt_xdate()     # 自動旋轉
plt.show()