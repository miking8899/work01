# ex4_1.py
class Queue():
    ''' Queue佇列 '''
    def __init__(self):
        self.queue = []             # 使用串列模擬

    def enqueue(self, data):
        ''' data插入佇列 '''
        self.queue.insert(0, data)
        print('成功插入 %s 至佇列' % data)

    def size(self):
        ''' 回傳佇列長度 '''
        return len(self.queue)
    
q = Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print('佇列長度是 : ', q.size())











