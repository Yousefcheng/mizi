'''
    输入两个整数A、B以及一个运算符（包括加,减,乘,除,整除,取余,幂），输出计算等式。如果是非法计算，输出ERROR。
'''
num1 = input()
num2 = input()
symbol = input()
try:
    num1 = int(num1)
    num2 = int(num2)
    if(symbol == '+'):

        result = num1+num2
        print(f"{num1}{symbol}{num2}={result}")

    elif (symbol == '-'):

        result = num1-num2
        print(f"{num1}{symbol}{num2}={result}")

    elif(symbol == '*'):

        result = num1*num2
        print(f"{num1}{symbol}{num2}={result}")

    elif (symbol == '/'):

        result = num1/num2
        print(f"{num1}{symbol}{num2}={result}")

    elif (symbol == '%'):

        result = num1 % num2
        print(f"{num1}{symbol}{num2}={result}")

    elif (symbol == '//'):

        result = num1//num2
        print(f"{num1}{symbol}{num2}={result}")

    elif (symbol == '**'):

        result = num1 ** num2
        print(f"{num1}{symbol}{num2}={result}")
    else:
        print('ERROR')
        
except:
    print('ERROR')
