# !/usr/bin/env python
# coding=utf-8
# 示範while的用法

number = 1
while number < 10:
    number += 1
    if not number%2 == 0: # 不是雙數時則略過本輪循環
        continue
    else: 
        print number      # 輸出雙數2、4、6、8、10
#以上輸出2，4，6,8,10這些偶數 
 
 number = 1
while True:              # 條件是True表示一直執行 
    print number         # 輸出1到5
    number = number+1
    if number > 5:       # 當i大於5時跳離循環體
        break
# 以上輸出1,2,3,4,5

