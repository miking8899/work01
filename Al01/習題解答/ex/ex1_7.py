# ex1_7.py
import itertools

x = ['北京', '天津', '上海', '廣州', '武漢']
perm = itertools.permutations(x)
n = 0
for i in perm:
    n += 1
    print(i)
print(f"總共有 {n} 拜訪方式")




















