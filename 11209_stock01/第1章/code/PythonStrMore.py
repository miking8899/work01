# !/usr/bin/env python
# coding=utf-8

print "Hello 'World'"       # 雙引號單引號夾雜使用
print 'Hello "World"'       # 單引號裡套雙引號
print "Hello: \name is Peter." # \n是換行符
print r"Hello \name is Peter." # 加了前綴r，則會原樣輸出
str = "123456789"
print str.index("234")   	# 查詢234這個字串的位置，傳回1 
#print str.index("256")  	# 沒找到則會拋出例外
print str.find("456")    	# 查詢456所在的位置，傳回3
print str.find("256")    	# 沒找到，傳回-1
print len(str)            	# 傳回長度，結果是9
print str.replace("234", "334")  # 把234置換成334

