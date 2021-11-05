list=input()
num=int(input())
list=list.split(',')

list=[int(i) for i in list]

# print(list)

if num in list:
    print(list.index(num))
else:
    list.append(num)
    # print(list)
    list=sorted(list)
    print(list.index(num))

