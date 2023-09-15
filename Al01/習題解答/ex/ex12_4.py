# ex12_4.py
""" 參數 size 代表皇后數 """
class Queens:
    def __init__(self, size):
        self.size = size        # 皇后數
        self.solutions = 0      # 解答數
        self.solve()

    def solve(self):
        print(f"輸出結果")
        print("="*30)
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print(f"找到 {self.solutions} 個解答")

    def put_queen(self, positions, target_row):
        if target_row == self.size:             # 完成所有皇后位置設定
            self.displayboard(positions)        # 繪製皇后棋盤  
            self.solutions += 1                 # 解答加 1
        else:
            # 每一行要找皇后位置
            for column in range(self.size):
                if self.is_OK(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def is_OK(self, positions, ocuppied_rows, column):
        for i in range(ocuppied_rows):
            if positions[i] == column \
                or positions[i] - i == column - ocuppied_rows  \
                or positions[i] + i == column + ocuppied_rows:
                return False
        return True

    def displayboard(self, positions):
        """ 顯示 8 皇后結果"""
        for row in range(self.size):
            boardrow = ""
            for column in range(self.size):
                if positions[row] == column:
                    boardrow += "Q "
                else:
                    boardrow += "1 "
            print(boardrow)
        print("="*30)

Queens(4)

