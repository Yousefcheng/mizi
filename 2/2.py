numList=input()

numList=numList.split(',')
numList=[int(i) for i in numList]
res={}
numSet=set(numList)
numSet=sorted(numSet)
# print(numSet)
# print(numList)
for i in numSet:
    res[i]=numList.count(i)

print(res)