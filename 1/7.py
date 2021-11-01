def get_common_str(list_a):
    '''输入列表a，返回公共子串
    输入: ["flower","flow","flight"]
    输出: "fl"
    输入: ["dog","racecar","car"]输出: ""
    '''
    if len(list_a) == 0:
        return ''
    common_str = ''  # 公共字符串

    # 先找出最短的字符串
    min_str = min(list_a, key=lambda x: len(x))
    # print(min_str)  # 最短的字符串flow
    for i in range(len(min_str)):
        flag = False  # 退出外部循环标志
        for j in list_a:
            if min_str[i] != j[i]:
                common_str = min_str[:i]
                flag = True
                break
        if flag:
            break
    else:
        return min_str

    return common_str
num1=int(input())
word=[]
while(num1):
    temp=input()
    word.append(temp)
    num1=num1-1


print(get_common_str(word))