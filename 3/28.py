'''
    双重循环过于简单
'''

def add_num(num):
    if num==1:
        return 1
    else:
        temp=''
        for i in range(num-1):
            
            temp=temp+'1'
            
        temp=temp+'2'
            # sum=sum+int(temp)
            # temp=temp[0:-1]
        return int(temp)

n=int(input())

sum=0
for i in range(1,n+1):
    # print(add_num(i))
    sum=sum+add_num(i)


print(sum)
