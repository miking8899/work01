# ex6_1.py
class Node():
    def __init__(self, data=None):
        ''' 建立二元樹的節點 '''
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        ''' 建立二元樹 '''
        if self.data:                           # 如果根節點存在
            if data < self.data:                # 插入值小於目前節點值
                if self.left:
                    self.left.insert(data)      # 遞迴呼叫往下一層
                else:
                    self.left = Node(data)      # 建立新節點存放資料
            else:                               # 插入值大於目前節點值
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)                
        else:                                   # 如果根節點不存在
            self.data = data                    # 建立根節點
            
    def preorder(self):
        ''' 前序列印 '''
        print(self.data)                        # 列印
        if self.left:                           # 如果左子節點存在
            self.left.preorder()                # 遞迴呼叫下一層        
        if self.right:                          # 如果右子節點存在
            self.right.preorder()               # 遞迴呼叫下一層        

    def count(self):
        global num
        if self.left:                           # 如果左子節點存在
            self.left.count()                   # 遞迴呼叫下一層
        if self.left == None and self.right == None:
            num += 1
        if self.right:                          # 如果右子節點存在
            self.right.count()                  # 遞迴呼叫下一層

num = 0        
tree = Node()                                   # 建立二元樹物件
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32] # 建立二元樹數據
for d in datas:
    tree.insert(d)                              # 分別插入數據
print("所建的二元樹前序列印如下 : ")
tree.preorder()                                 # 前序列印
tree.count()
print("葉節點數量 = ", num)





    















