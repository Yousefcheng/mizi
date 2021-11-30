'''
    给定一个字符串s，s中只包含大写字母、小写字母、数字、空格。从第一个字符开始按序统计前三种类型字符的数目，注意如果遇到空格直接跳过。（提示：需要分别创建三个初始值为0的变量记录统计结果）
    
    只包含大写字母、小写字母、数字、空格的字符串s

    用空格隔开的三个数字，表示三种字符的数量
    aB 1a
'''

s = input()

upper = 0
lower = 0
num = 0

for strs in s:
    # 如果在字符串中有小写字母，那么小写字母的数量+1

    if strs.islower():
        lower += 1

    # 如果在字符串中有数字，那么数字的数量+1
    elif strs.isdigit():
        num += 1
    elif strs.isupper():  # 大写字母
        upper += 1

print(upper,lower,num)
