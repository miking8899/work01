import math
money = 2000


def sum():
    money = 1
    money += 1
    print(money)
    return


print("money : ", money)
sum()
print("money update no change because global var :", money)


print("dir list ", dir(math))
