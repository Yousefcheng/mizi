'''
    
'''
class computer:
    def __init__(self, num1, op, num2) -> None:
        self.num1 = num1
        self.num2 = num2
        self.op = op

    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2

    def divide(self):
        return self.num1//self.num2


num1, op, num2 = input().split()
num1, num2 = int(num1), int(num2)

A = computer(num1, op, num2)
if __name__ == '__main__':
    if op == '+':
        print(A.add())
    if op == '-':
        print(A.sub())
    if op == '*':
        print(A.multiply())
    if op == '/':
        print(A.divide())
