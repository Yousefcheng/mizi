# from math import *
import numpy as np


'''
    海伦公式求面积
'''
def heron(a,b,c):
    p=(a+b+c)/2
    S=(p*(p-a)*(p-b)*(p-c))**0.5
    return S

'''
求各个边的边长,输入三个数组
'''
def norm(a,b,c):
    ab=( (b[0]-a[0])**2+(b[1]-a[1])**2 ) ** 0.5
    ac=( (a[0]-c[0])**2+(a[1]-c[1])**2 ) ** 0.5
    bc=( (b[0]-c[0])**2+(b[1]-c[1])**2 ) ** 0.5

    return ab,ac,bc

# 面积除以边长  得到高  也就是点到直线的距离    
def get_res(a,b,S):
    ab=( (b[0]-a[0])**2+(b[1]-a[1])**2 ) ** 0.5
    res=S/ab*2
    return res


res_list=[]


x=eval(input())
y=eval(input())
dot=eval(input())

for i in range(3):
    ab,ac,bc=norm(x[i],y[i],dot)
    S=heron(ab,ac,bc)
    res=get_res(x[i],y[i],S)
    res_list.append(res)


res_list = np.array(res_list)
print(res_list)

