# coding=utf-8
import re
# 以等號分隔，輸出等號兩邊的字串['content', 'Hello World']
print(re.split('=','content=Hello World')) 
# 輸出等號左邊的字串content
print(re.split('=','content=Hello World')[0]) 
# 輸出等號右邊的字串Hello World
print(re.split('=','content=Hello World')[1]) 

str = 'content=code:(600001),price:(20)'
pattern = re.compile(r'[(](.*?)[)]')
# 輸出括號內的所有內容['600001', '20'] 
print(re.findall(pattern, str))

# 取得<>之間的所有內容
rule = r'<(.*?)>'
result = re.findall(rule, 'content=<123>')
print(result)   # 輸出['123']

# 取得引號之間的內容
rule = r'"(.*?)"'
result = re.findall(rule, 'content="456"')
print(result)   # 輸出['456']

# 用逗點分隔
str='600001,10,12,15'
item=re.split(',',str) 
print(item)     # 輸出['600001', '10', '12', '15']