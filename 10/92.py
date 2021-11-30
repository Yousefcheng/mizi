# (1+a*x)**3+(1+b*x)**3


from sympy import *

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
express=eval(input())

res=simplify(express)

print(res)


# import sympy 
from sympy import * 
  
x = symbols('x') 
expr = sin(x) 
     
# Use sympy.lambdify() method 
f = lambdify(x, expr, "math")  
    
print("Using lambda function in SymPy to evaluate sin(90) : {}".format(f(90))) 