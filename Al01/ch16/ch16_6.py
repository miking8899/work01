# ch16_6.py

def longest_common_substring(word1, word2):
   # 建立表格
   cell = [[0] * (1 + len(word2)) for i in range (1 + len(word1))]
   longest = 0                            # 預設最長共用子字串長度
   for x in range(1, 1 + len(word1)):
       for y in range(1, 1 + len(word2)):
           if word1[x-1] == word2[y-1]:
               cell[x][y] = cell[x - 1][y - 1] + 1
               if cell[x][y] > longest:
                   longest = cell[x][y]
   return longest
wd1 = 'python'
wd2 = 'pythonic'
lcs = longest_common_substring(wd1, wd2)
print(f"{wd1} 和 {wd2} 的最長共用子字串長度是 {lcs}")
wd3 = 'substring'
wd4 = 'strings'
lcs = longest_common_substring(wd3, wd4)
print(f"{wd3} 和 {wd4} 的最長共用子字串長度是 {lcs}")


