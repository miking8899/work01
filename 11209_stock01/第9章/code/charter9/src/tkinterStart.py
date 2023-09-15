# !/usr/bin/env python
# coding=utf-8
import tkinter
import tkinter.messagebox 
loginWin = tkinter.Tk()
loginWin.geometry('220x120')    # 設定大小
loginWin.title('登入視窗')      # 設定視窗標題
# 放置兩個Label標簽
tkinter.Label(loginWin,text='使用者名稱：').place(x=10,y=20)
tkinter.Label(loginWin,text='密 碼：').place(x=10,y=50)
userVal = tkinter.StringVar()
pwdVal = tkinter.StringVar()
# Entry是用來接受字串的控制項
userEntry = tkinter.Entry(loginWin,textvariable=userVal)
userEntry.place(x=65,y=20)
pwdEntry = tkinter.Entry(loginWin,textvariable=pwdVal,show='*')  # 用*號代替輸入文字
pwdEntry.place(x=65,y=50)
def check():    # 定義登入按鈕的處理函數（即定義點選登入按鈕時觸發的方法）
    userName=userVal.get()
    pwd=pwdVal.get()
    print('使用者名稱:'+ userName)
    print('密碼:'+pwd)
    if(userName=='python' and  pwd =='kdj'):
        tkinter.messagebox.showinfo('提示','登入成功') 
    else:           
        tkinter.messagebox.showinfo('提示','登入失敗')
tkinter.Button(loginWin,text='登入',width=12,command=check).place(x=10,y=85)
tkinter.Button(loginWin,text='離開',width=12,command=loginWin.quit).place(x=120,y=85)
tkinter.mainloop()