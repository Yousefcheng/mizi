string = input().split()
num_list = []
output_list = []
sum = 0

for i in string:
    if not i.isalpha():
    # if 1:    
        num_list.append(eval(i))
        # num_list.append(i)
        output_list.append(eval(i))
        # output_list.append(i)
    else:
        output_list.append(str(i))

for i in num_list:
    sum = sum+i

print(output_list)
print(sum)
