'''
    
'''
num = int(input())

category =1 if (not num % 4) and (num % 100) else 0

# print(category)

if category:
    print(366)
else:
    print(365)