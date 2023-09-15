# ch19_4.py
n = eval(input('輸入整數 n = '))

r = ''                      # 結果字串
while n > 0:
    r = str(n % 2) + r
    n //= 2
print(r)



