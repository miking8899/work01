# ch6_4.py
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

    def inorder(self):
        ''' 中序列印 '''
        if self.left:                           # 如果左子節點存在
            self.left.inorder()                 # 遞迴呼叫下一層
        print(self.data)                        # 列印
        if self.right:                          # 如果右子節點存在
            self.right.inorder()                # 遞迴呼叫下一層
        
tree = Node()                                   # 建立二元樹物件
datas = [10, 21, 5, 9, 13, 28]                  # 建立二元樹數據
for d in datas:
    tree.insert(d)                              # 分別插入數據
tree.inorder()                                  # 中序列印




    















