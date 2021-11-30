'''
    
'''
num1=int(input())
num2=int(input())

people=[i for i in range(num1)]
res=0
relation=[]

while(num2):
    temp=[int(i) for i in input().split()]
    relation.append(temp)
    num2=num2-1

for i in relation:
    # print(i)
    people[i[1]]=people[i[0]]

res=len(set(people))
print(res)
