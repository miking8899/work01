# !/usr/bin/env python
# coding=utf-8
# 透過lambda表達式定義了一個匿名函數
add = lambda a,b,c:a+b+c
print(add(1,2,3)) # 輸出6
# 計算奇數
numbers = [1, 3, 6, 7, 10,11]   
# 與filter整合使用
numbers = filter(lambda input: input%2!=0, numbers)
print numbers #[1, 3, 7, 11]
numbers = [2, 3, 4]
# 與map整合使用
numbers = map(lambda x: x*x, numbers)
print numbers #[4, 9, 16]
# 與reduce整合使用
numbers = [1,2,3,4,5]   
sum = reduce(lambda x, y: x + y, numbers)
print sum # 輸出15
# 與sorted整合使用
numbers = [1,-2, 3, -4,5]
numbers = sorted(numbers, lambda x, y: abs(y)-abs(x))
print numbers # [5, -4, 3, -2, 1]