'''
    
'''
student=[int(i) for i in input().split()]

target=int(input())

res=0
for i in range(len(student)):
    sum=0
    for j in range(i+1,len(student)):
        for m in range(j+1,len(student)):
            sum=student[i]+student[j]+student[m]
            if sum<target:
                res=res+1
            
print(res)