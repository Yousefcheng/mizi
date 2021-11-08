''' 
    这道题本来可以用暴力破解，但是机智的我用了一个巧妙的算法：
        选出最大值，然后在原列表中剔除最大值相邻的值，分三种情况：最大值分别在最左边界，中间和最右边界
        然后再剩下的列表中选出第二个最大值，然后加起来

        机智如我
'''


list=input()

list=list.split()

# print(list)
list=[int(i) for i in list]

first_max=max(list)
# print(first_max)

max_idx=list.index(first_max)

if max_idx==len(list)-1:
    del list[max_idx]
    del list[max_idx-1]
elif max_idx==0:
    del list[1]
    del list[0]
else:
    del list[max_idx+1]
    del list[max_idx]
    del list[max_idx-1]

secend_max=max(list)
print(secend_max+first_max)
