# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import *
win = Tk()
win.title("tkinter and matplotlib")
figure = plt.figure()  
# 把用matplotlib繪制的動作定義在方法中，方便呼叫
def drawPlotOnCancas():      
    ax = figure.add_subplot(111)
    ax.set_title('Matplotlib整合tkinter')
    x = np.array([1,2,3,4,5])
    ax.plot(x, x*x)
    plt.rcParams['font.sans-serif']=['SimHei']
# 在Canvas上顯示基於matplotlib的物件
canvs = FigureCanvasTkAgg(figure, win)
canvs.get_tk_widget().pack()
drawPlotOnCancas()
win.mainloop()