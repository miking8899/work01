# ch5_5.py
def factorial(n):
    global fact
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        print(f"factorial({n})呼叫前 {n}! = {fact}")
        print("到達遞迴條件終止 n = 1")
        fact = 1
        print(f"factorial({n})返回後 {n}! = {fact}")
        return fact
    else:
        print(f"factorial({n})呼叫前 {n}! = {fact}") 
        fact = n * factorial(n-1)
        print(f"factorial({n})返回後 {n}! = {fact}")
        return fact

fact = 0
N = eval(input("請輸入階乘數 : "))
print(f"{N} 的階乘結果是 = {factorial(N)}")





    
