# ch19_3.py
money = eval(input('輸入金額 : '))
price = input('商品金額 : ')
change = int(money) - int(price)
print("找零結果如下 :")

coin = [500, 100, 50, 10, 5, 1]
wd = ["500元紙鈔", "100元紙鈔", "50元硬幣",
      "10元硬幣", "5元硬幣", "1元硬幣"]

for c, w in zip(coin,wd):
    r = change // c
    change %= c
    print(f"{w} : {r}")


