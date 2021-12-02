'''
    
'''

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False
str_list = input().split()
num_list = []
output_list = []
sum = 0

for i in str_list:
    # print(i)
    # print(i.is_number())
    if is_number(i):    
        if '.' in i:
            output_list.append(float(i))
            num_list.append(float(i))
        else:
            output_list.append(int(i))
            num_list.append(int(i))
    
    else:
        output_list.append(str(i))


for i in num_list:
    sum = sum+i

print(output_list)
print(sum)
