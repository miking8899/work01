# !/usr/bin/env python
# coding=utf-8
import tkinter
win = tkinter.Tk()
win.title("復選框")
win.geometry("150x160")
# 加入Label標簽
tkinter.Label(win,text='我已經掌握的寫程式語系').pack(anchor=tkinter.W)
# 點選復選框後觸發的函數
def handleFunc():
    msg = ''
    # 勾選為True，不選為False，下同
    if pythonSelected.get() == True: 
        msg += pythonCheckButton.cget('text');
        msg+='\n'        
    if javaSelected.get() == True:
        msg += javaCheckBotton.cget('text')
        msg+='\n'
    if goSelected.get() == True:
        msg += goCheckBotton.cget('text')
        msg += "\n"    
    text.delete(0.0,tkinter.END)
    text.insert('insert',msg)
# 建立復選框
pythonSelected = tkinter.BooleanVar()
pythonCheckButton = tkinter.Checkbutton(win,text='Python',variable=pythonSelected,command=handleFunc)
pythonCheckButton.pack(anchor=tkinter.W)
javaSelected = tkinter.BooleanVar()
javaCheckBotton = tkinter.Checkbutton(win,text='Java',variable=javaSelected,command=handleFunc)
javaCheckBotton.pack(anchor=tkinter.W)
goSelected = tkinter.BooleanVar()
goCheckBotton = tkinter.Checkbutton(win,text='Go',variable=goSelected,command=handleFunc)
goCheckBotton.pack(anchor=tkinter.W)
# 建立一個多行文字框
text = tkinter.Text(win,width=20,height=5)
text.pack(anchor=tkinter.W)
win.mainloop()