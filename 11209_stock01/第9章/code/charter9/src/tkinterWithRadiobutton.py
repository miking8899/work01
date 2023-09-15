# !/usr/bin/env python
# coding=utf-8
import tkinter
win = tkinter.Tk()
win.title("單選框")
win.geometry("200x150")
# 建立標簽
tkinter.Label(win,text='您目前學的是:').pack()
# 定義選取單選框後執行的動作
def handleSelected():
    text.delete(0.0,tkinter.END)
    text.insert('insert',selectVal.get())
# 建立單選項
selectVal = tkinter.StringVar()
selectVal.set('Python')
pythonSelect = tkinter.Radiobutton(win,text='Python',value='Python',variable=selectVal,command=handleSelected).pack()
javaSelect = tkinter.Radiobutton(win,text='Java',value='Java',variable=selectVal,command=handleSelected).pack()
# 建立多行文字框
text = tkinter.Text(win,width=20,height=3)
text.pack()
win.mainloop()