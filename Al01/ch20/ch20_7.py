# ch20_7.py
def distributeCandies(candies, num_people):
    result = [0] * num_people           # 儲存結果串列
    nxt = 0
    while candies > 0:
        result[nxt % num_people] += min(nxt + 1, candies)
        nxt += 1                        # 下一位
        candies -= nxt                  # 剩下糖果數
    return result

print(distributeCandies(8, 4))
print(distributeCandies(12, 3))










      



    





        





