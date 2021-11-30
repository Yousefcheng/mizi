'''
    
'''
from math import *

class Circle:
    def __init__(self,center_x,center_y,r) -> None:
        self.center_x,self.center_y=center_x,center_y
        self.r=r
        # print(self.center_x)

    def computer_relation(self,x,y):
        if abs(x-self.center_x)**2+abs(y-self.center_y)**2 <= self.r**2:
            print(1)
        else:
            print(-1)



x,y,center_x,center_y,r=[int(i) for i in input().split()]
A=Circle(center_x,center_y,r)
A.computer_relation(x,y)