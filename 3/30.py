'''
    你手算一下就会发现：实际上是一个斐波那契数列   用递归求解即可
'''
def fib(num):
    if num==1:
        return 1
    elif num==2:
        return 2
    else:
        return fib(num-1)+fib(num-2)

num=int(input())
print(fib(num))