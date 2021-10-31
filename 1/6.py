"""
输入一个四位正整数和两个一位正整数，对第一个正整数进行加密并输出。加密的规则如下：第一个数字加上第二个数字，
然后用和除以第三个正整数的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

输入为三行，第一行为四位正整数，第二三行都为一位正整数。
"""

num1 = int(input())
num2 = int(input())
num3 = int(input())

temp = (num1+num2) % num3
num_1 = int(temp/1000 % 10)
num_2 = int(temp/100 % 10)
num_3 = int(temp/10 % 10)
num_4 = int(temp % 10)

print(num_4*1000+num_1+num_3*100+num_2*10)
