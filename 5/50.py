'''
    
'''
class Stack:
    def __init__(self) -> None:
        self.items = []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def output(self):
        return self.items

ops=[]

while(1):
    op=[int(i) for i in input().split()]
    if op[0]==0:
        break
    else:
        ops.append(op)

stack=Stack()

for i in ops:
    if i[0]==1:
        stack.push(i[1])
    elif i[0]==2:
        stack.pop()

print(" ".join(str(i) for i in stack.output()))
