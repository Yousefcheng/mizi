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
