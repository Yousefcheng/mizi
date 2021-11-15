'''
    双重循环过于简单
'''
n=int(input())

sum=1
for i in range(n-1):
    temp=''
    for i in range(n-1):
        temp=temp+'1'
    temp=temp+'2'

    sum=sum+eval(temp)
print(sum)
