import time
import calendar

ticks = time.time()

print("時截: ", ticks)


localtime = time.asctime(time.localtime(time.time()))

print("Local time : ", localtime)
# 格式化成2016-03-20 11:45:39形式
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print(" Time :", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

cmonth = calendar.month(2023, 10)

print(" 月 曆")
print(cmonth)
