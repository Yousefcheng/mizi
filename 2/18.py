string = input().split
num_list = []
output_list = []


for i in string:
    if not i.isalpha():
        num_list.append(eval(i))
        output_list.append(eval(i))
    else:
        output_list.append(i)
sum = 0
for i in num_list:
    sum = sum+i

print(output_list)
print(sum)
