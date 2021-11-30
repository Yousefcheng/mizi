'''
    
'''
grade=input()

try:
    grade=int(grade)
    if grade>=90 and grade<=100:
        print('A')
    elif grade>=80 and grade<90:
        print('B')
    elif grade>=70 and grade<80:
        print('C')    
    elif grade>=60 and grade<70:
        print('D')
    elif grade < 60 and grade>=0 :
        print('E')
    else:
        print('data error!')
except:
    print('data error!')