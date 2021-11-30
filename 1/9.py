'''
    
'''
def isone(ctx):
    # print(ctx[2:])
    ctx=[int(x) for x in list(ctx[2:]) ]
    if(all(ctx)):
        return True
    else:
        return False


count = int(input())
num = []
while(count):
    temp = int(input())
    num.append(bin(temp))
    count = count-1

for i, ctx in enumerate(num):
    if i == len(num)-1:
        print(isone(ctx), end='')
    else:
        print(isone(ctx), end=',')
