# ch20_5.py
def calPoints(ops):
    score = []
    for s in ops:
        if s == '+':            # '+', 得分是前2局的和
            score.append(score[-1] + score[-2])
        elif s == 'D':          # 'D',得分是前一局的2倍
            score.append(score[-1] * 2)    
        elif s == 'C':          # 'C'前一局得分不算
            score.pop()       
        else:
            score.append(int(s))
    return sum(score)
                         
print(calPoints(['3', '2', 'C', 'D', '+']))     
print(calPoints(['3','-2','4','C','D','9','+','+']))













      



    





        





