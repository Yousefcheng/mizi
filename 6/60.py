'''
    
'''
arr=[int(i) for i in input().split()]
num=int(input())

res=0
for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum=sum+arr[j]
        if sum==num:
            res=res+1
            break

print(res)