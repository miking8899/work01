#判斷字元是否重複的方法，就是判斷每個字元在字串中出現的次數，如果出現的次數大於 1 表示有重複，就用 repeat 串列紀錄，如果出現次數等於 1 表示沒有重複，就用 not_repeat 串列記錄，如此一來就能夠篩選出重複與不重複的字元。

while True:
    text=''
    text=input("請輸入一串文字測試重覆字元 :")
    repeat=[]
    non_repeat=[]

    for i in text:
        a=text.count(i,0,len(text))
        if a>0 and i not in repeat:
            repeat.append(i)
        if a==1 and i not in non_repeat:
            repeat.append(i)
    print (repeat)
    print (non_repeat)

