# !/usr/bin/env python
# coding=utf-8
# 示範for的用法

languages = ["Java", "Go", "C++", "Python", "C#"]
for tool in languages:
    if tool == "C++":
        continue # 不會輸出C++
    if tool == "Python":
        print("我正在學Python。")
        break
    print tool
# 輸出了Java，Go，我正在學Python，沒有輸出C#

