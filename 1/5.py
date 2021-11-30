'''
    
'''
def isRe_num(son):
    rev_son = reversed(list(son))
    if list(rev_son) == list(son):
        return True
    else:
        return False
num = int(input())
re_num = []
while num:
    temp = input()
    re_num.append(temp)
    num = num-1
    # print(num)

for index,son in enumerate(re_num):
    if index==len(re_num)-1:
        print(isRe_num(son),end='')
    else:
        print(isRe_num(son),end=',')



