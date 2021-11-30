''' 1
2
3
[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
'''

import numpy as np

choose=int(input())

num1=int(input())
num2=int(input())

arr=eval(input())
arr=np.array(arr)

if choose==0:
    arr[[num1,num2],:] = arr[[num2,num1],:]
else:
    arr[:,[num1,num2]] = arr[:,[num2,num1]]

print(arr)