'''
    
'''
data=input().split()
data=[int(i) for i in data]

res=[]
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[j]>data[i]:
            min=j-i
            res.append(min)
            break
        if j==len(data)-1:
            res.append(0)
res.append(0)
# print(res)

print(" ".join(str(i) for i in res)) 