# ch20_10.py
def lemonadeChange(bills):
    coins = {5:0, 10:0}             # 建立硬幣字典
    for bill in bills:              # 遍歷顧客所給的錢
        if bill == 5:               # 如果顧客給5元硬幣
            coins[5] += 1           # 5元硬幣數量加 1
        elif bill == 10:            # 如果顧客給10元硬幣
            if coins[5] == 0:       # 如果5元硬幣數量是 0
                return False        # 回應是 False
            else:
                coins[10] += 1      # 10元硬幣數量加 1
                coins[5] -= 1       # 5元硬幣數量減 1
        elif bill == 20:            # 如果顧客給20元
            if coins[10] > 0:       # 如果有10元硬幣
                if coins[5] == 0:   # 如果5元硬幣數量是 0
                    return False    # 回應是 False
                else:
                    coins[5] -= 1   # 5元硬幣數量減 1
                    coins[10] -= 1  # 10元硬幣數量減 1
            else:
                if coins[5] < 3:    # 5元硬幣數量少於 3
                    return False    # 回應是 False
                else:
                    coins[5] -= 3   # 5元硬幣數量減 3
    return True

print(lemonadeChange([5, 5, 5, 10, 20]))
print(lemonadeChange([5, 5, 10, 5]))
print(lemonadeChange([10, 5, 10]))
print(lemonadeChange([5, 5, 20, 10]))








      



    





        





