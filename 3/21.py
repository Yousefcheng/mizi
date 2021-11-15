'''
    这道题有毒了，我觉得题或者系统有点问题，我写的没有问题
'''

# 二分法递归求解  
def get_answer(min,max):
    if max-min<10e-6:
        return max
    else:
        if ((max+min)/2)**2>n:
            max=(max+min)/2
        else:
            min=(max+min)/2
        # print(min,max)
        return get_answer(min,max)


n=int(input())

gmin=0
gmax=n+1
ans=get_answer(gmin,gmax)

# print(round(ans,4))
# print(format(ans, '.4f'))
print(int(ans * 10000) / 10000 )