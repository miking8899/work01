#結構IF規則
import pyinputplus as pyip

message=""

while True:
    score=pyip.inputInt("請輸入成績(0~100) :",min=-1,max=100)
    if score<0:
        print("\n 程式結束")
        break
    if score>=90:
        message="優"
    elif score>=80:
        message="甲"
    elif score>=70:
        message="乙"
    elif score>=60:
        message="丙"
    else:
        message="丁"
    print("成績:",message)

        
