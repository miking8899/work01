# !/usr/bin/env python
# coding=utf-8
import tkinter as tk
from tkinter import ttk
win = tk.Tk() 
win.title("下拉框")    # 加入標題
tk.Label(win, text="選取寫程式語系").grid(column=0, row=0)    # 加入標簽  
# 建立下拉框 
comboboxVal = tk.StringVar() 
combobox = ttk.Combobox(win, width=12, textvariable=comboboxVal) 
combobox['values'] = ('Python', 'Java', '.NET','go')        # 設定下拉式選單的值 
combobox.grid(column=1, row=0)      # 設定其在界面中出現的位置，column代表列，row 代表行 
combobox.current(0)    # 設定下拉式選單的預設值 
# 清理並插入文字框的內容
def handle(): 
    text.delete(0,tk.END)
    text.insert(0,combobox.get()) 
# 建立按鈕 
button = tk.Button(win, text="選取", width=12,command=handle)
button.grid(column=1, row=1) 
# 建立文字框 
val = tk.StringVar()  
text = tk.Entry(win, width=12, textvariable=val)    # 建立文字框
text.grid(column=0, row=1)
text.focus()    # 預設設定焦點（游標）在文字框中
win.mainloop()  # 開啟主循環以監聽事件