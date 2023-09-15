# ch19_2.py
money = eval(input('輸入金額 : '))
price = input('商品金額 : ')
change = int(money) - int(price)
print("找零結果如下 :")
n500 = change // 500            # 找零500元紙鈔     
q500 = change % 500             # 餘額
print(f'500元紙鈔 : {n500}')

n100 = q500 // 100              # 找零100元紙鈔
q100 = q500 % 100               # 餘額
print(f'100元紙鈔 : {n100}')

n50 = q100 // 50                # 找零50元硬幣
q50 = q100 % 50                 # 餘額
print(f'50元硬幣 : {n50}')

n10 = q50 // 10                 # 找零10元硬幣
q10 = q50 % 10                  # 餘額
print(f'10元硬幣 : {n10}')

n5 = q10 // 5                   # 找零5元硬幣
q5 = q10 % 5                    # 餘額
print(f'5元硬幣 : {n5}')

print(f'1元硬幣 : {q5}')   # 找零1元硬幣


