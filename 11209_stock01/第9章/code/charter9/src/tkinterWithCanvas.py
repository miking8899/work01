# !/usr/bin/env python
# coding=utf-8
import tkinter as tk
win = tk.Tk()
win.title('Cavas畫布')    # 設定視窗標題
win.geometry("550x350")
canvas = tk.Canvas(win,background='white',width=500,height=300)
canvas.pack()
# 繪制直線
canvas.create_line((0, 0), (60, 60), width=2, fill="red")
# 繪制圓弧
canvas.create_arc((210, 210), (280, 280),fill='yellow',width=3)
# 繪制矩形
canvas.create_rectangle(75, 75, 120, 120, fill='green', width=2)
# 顯示文字
canvas.create_text(350, 200,text='示範文字效果')
# 繪制圓或橢圓，取決於外接矩形
canvas.create_oval(150, 150, 200, 200,fill='red')
# 連線由參數特殊的點，繪制多邊形
point = [(280, 260), (300, 200), (350, 220),(400,280)]
canvas.create_polygon(point, outline='green', fill='yellow')
win.mainloop()