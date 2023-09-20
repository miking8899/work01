#結構IF規則
import pyinputplus as pyip

message=""

while True:
    score=pyip.inputInt("請輸入成績(0~100) :",min=0,max=100)
   
    if score>=90:
        message="優"
    else:
        if score>=80:
            message="甲"
        else:
            if score>=70:
                    message="乙"
            else :
                if score>=60:
                    message="丙"
                else:
                    message="丁"
    print("成績:",message)

        
