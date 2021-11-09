'''
递归求解
'''
def n_sum(n):
    if n==1:
        return 1
    else:
        return n_sum(n-1)+n

n=int(input())
print(n_sum(n))