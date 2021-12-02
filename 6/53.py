'''
    
'''
class LoopQueue(object):
    def __init__(self, n=10):
        self.arr = [None] * (n+1)  # 由于特意浪费了一个空间，所以arr的实际大小应该是用户传入的容量+1
        self.front = 0
        self.tail = 0
        self.size = 0

    def is_full(self):
        return (self.tail+1) % len(self.arr) == self.front  
    def is_empty(self):
        # 判断队列是否为空
        return self.size == 0
    def enqueue(self, e):
        # 入队
        if self.is_full():
            return False  # 如果队列满，以当前队列容积的2倍进行扩容
        self.arr[self.tail] = e
        self.tail = (self.tail+1) % len(self.arr)
        self.size += 1
        return True

    def dequeue(self):
        # 出队
        if self.is_empty():
            return -1

        result = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front+1) % len(self.arr)
        self.size -= 1
        return result   

n=int(input())
m=int(input())
ops=[]
for i in range(m):
    op=[int(i) for i in input().split()]
    ops.append(op)

loop=LoopQueue(n)

for i in ops:
    if i[0]==1:
        print(loop.enqueue(i[1]))
    elif i[0]==2:
        print(loop.dequeue())