# ex1_2.py   
def fun(n):
    if n == 1:
        return 1
    else:
        return fun(n - 1) + 1.0 / n

n = eval(input('請輸入整數 : '))
for i in range(1, n + 1):
    print(f"{i}) = {fun(i):5.3f}")           

