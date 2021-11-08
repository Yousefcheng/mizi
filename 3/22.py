'''
    实际上是一个多循环分类的问题，过于简单
'''
sum=0
for x in range(1,10):
    for y in range(1,10):
        if x==y:
            continue
        for z in range(1,10):
            if x==z or y==z:
                continue
            for m in range(1,10):
                if x==m or y==m or z==m:
                    continue
                for n in range(1,10):
                    if x==n or y==n or z==n or m==n:
                        continue
                    # print(n)
                    if (x*10+y)*(z*100+m*10+n)==(x*100+m*10+y)*(z*10+n):
                        sum=sum+1

print(sum)