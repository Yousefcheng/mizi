'''
    
'''
import math

class Person:
    def __init__(self) -> None:
        name,weight,height,gender=input().split()
        self.__bmi=0
        self.name=name
        self.weight=int(weight)
        self.height=int(height)
        self.gender=gender
        
        if self.gender=='female':
            self.__bmi=math.floor((self.height-70)*0.6)
        else:
            self.__bmi=math.floor( (self.height-80)*0.7 )
    
    def print_bmi(self):
        print(self.__bmi)
    
        
A=Person()
A.print_bmi()