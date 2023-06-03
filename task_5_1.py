def calculate(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
    elif sign == '/':
        if b != 0:
            return a / b
        else:
            return 'Error: division by 0'
    elif sign == '0':
        return 'END'
    else:
        return 'Uncorrected sign'


sign = '-1'
while sign != '0':
    x = (input('input X'))
    y = (input('input Y'))
    sign = input('input SIGN')
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        result = calculate(x,y,sign)
        print(result)
    else:
        print('Uncorrected X or Y')
