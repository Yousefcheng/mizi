num_list=input()

num_list=num_list.split()
num_list=[int(i) for i in num_list]
# print(num_list)
rev_num_list=list(reversed(num_list))
# print(rev_num_list)
res = [(num_list[i]+rev_num_list[i]) for i in range(0,len(num_list))]

print(tuple(res))