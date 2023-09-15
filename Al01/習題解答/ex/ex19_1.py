# ex19_1.py
money = eval(input('輸入金額 : '))
price = input('商品金額 : ')
change = int(money) - int(price)
print("找零結果如下 :")
n500, q500 = divmod(change, 500)
print(f'500元紙鈔 : {n500}')

n100, q100 = divmod(q500, 100)
print(f'100元紙鈔 : {n100}')

n50, q50 = divmod(q100, 50)
print(f'50元硬幣 : {n50}')

n10, q10 = divmod(q50, 10)
print(f'10元硬幣 : {n10}')

n5, q5 = divmod(q10, 5)
print(f'5元硬幣 : {n5}')

print(f'1元硬幣 : {q5}')   # 找零1元硬幣


