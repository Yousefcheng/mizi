import numpy

num=int(input())

res=[]
for i in range(num+1):
    temp=list([i for i in range(i,num+i)])
    res.append(temp)

res=numpy.array(res)
print(res)