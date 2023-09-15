# ex1_5.py
def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

n = 20
times = 0.0000000001 * factorial(n)
print(f"排列組合需要 {times} 秒")








    
