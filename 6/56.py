'''
    
'''
num_list=input().split()

res=[]
for i in num_list:
    if num_list.count(i)==1:
        res.append(int(i))
res.sort()
print(res)