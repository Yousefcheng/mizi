numList=input() 
numList=numList.split(' ')
numList=[int(i) for i in numList]

new_numList=[abs(i) for i in numList]

print(f"{len(numList)},{max(numList)},{min(numList)},{sum(numList)}")
print(sorted(new_numList))