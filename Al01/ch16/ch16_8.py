# ch16_8.py

def longest_common_substring(word1, word2):
   # 建立表格
   cell = [[0] * (1 + len(word2)) for i in range (1 + len(word1))]
   longest = 0                            # 預設最長共用子序列長度
   for x in range(1, 1 + len(word1)):
       for y in range(1, 1 + len(word2)):
           if word1[x-1] == word2[y-1]:   # 字母相同  
               cell[x][y] = cell[x - 1][y - 1] + 1    # 左上方值 +1
               if cell[x][y] > longest:
                   longest = cell[x][y]   # 計算最大值
           else:
               # 取上方與左邊最大值
               cell[x][y] = max(cell[x-1][y], cell[x][y-1]) 
   return longest
wd1 = 'test'
wd2 = 'text'
lcs = longest_common_substring(wd1, wd2)
print(f"{wd1} 和 {wd2} 的最長共用子序列長度是 {lcs}")
wd3 = 'abcde'
wd4 = 'ace'
lcs = longest_common_substring(wd3, wd4)
print(f"{wd3} 和 {wd4} 的最長共用子序列長度是 {lcs}")
wd5 = 'abc'
wd6 = 'def'
lcs = longest_common_substring(wd5, wd6)
print(f"{wd5} 和 {wd6} 的最長共用子序列長度是 {lcs}")

