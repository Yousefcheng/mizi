'''

过于简单
'''
def solution(num_list,num):
    if num in num_list:
        print(num_list.index(num))
    else:
        print(-1)
num_list=input()
num=int(input())
num_list=num_list.split()
num_list=[int(i) for i in num_list]

solution(num_list,num)

# print(num_list.index(num))