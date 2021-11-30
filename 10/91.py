from sympy import *


express,sym=input().split()
express='Eq(f(x).diff(x,x)-3*f(x).diff(x)+f(x),sin(x))'
# # sym='x'
f=Function('f')
# # print(eval(express))
x = Symbol(sym)


eq_left=express[3:-1].rsplit(',',1)[0]
eq_right=express[3:-1].rsplit(',',1)[-1]

# # print(eval(eq_left))
eq_left=eval(eq_left)
eq_right=eval(eq_right)
res=dsolve(Eq(eq_left,eq_right),f(x))
print(res)

# Eq(f(x).diff(x,x)-3*f(x).diff(x)+f(x),sin(x)) x