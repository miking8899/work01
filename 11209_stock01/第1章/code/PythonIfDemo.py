# !/usr/bin/env python
# coding=utf-8

# 判斷閏年
year=2018
# year=2020
if (year%4 == 0) and (year%100 != 0):
    print("%d是閏年" %year)
elif year%400 == 0:
    print("%d是閏年" %year)
else:
    print("%d不是閏年" %year)

