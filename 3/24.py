'''
    
'''

input_list = [int(i) for i in input().split()]

res=0
front=1
back=1
front_temp=0
back_temp=0
for i in range(len(input_list)+1):

    for m in sorted(list(range(0,i)),reverse=True):
        if sorted(input_list[m:i])==input_list[m:i]:
            # print(input_list[m:i])
            if front_temp<len(input_list[m:i]):
                front_temp=len(input_list[m:i])
        else:
            break

    for n in range(i,len(input_list)+1):
        if sorted(input_list[i:n],reverse=True)==input_list[i:n]:
            # print(input_list[i:n])
            if back_temp<len(input_list[i:n]):
                back_temp=len(input_list[i:n])
        else:
            break
    if front_temp==1 or back_temp==1 or front_temp==0 or back_temp==0:
        continue
    else:
        front=front_temp
        back=back_temp


# print(front)
# print(back)

# print(front)
# print(back)
res=front+back-1
if res<3:
    res=0

print(res)

