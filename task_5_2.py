def sum_of_digits(number):
    result = 0
    if number >= 0:
        num = number
    else:
        num = -1 * number
    while num > 0:
        result += num % 10
        num = num // 10
    return result


def mut_of_digits(number):
    result = 1
    if number >= 0:
        num = number
    else:
        num = -1 * number
    while num > 0:
        result *= num % 10
        num = num // 10
    return result


n = int(input('input number '))
print('Sum = ', sum_of_digits(n))
print('Multiplication = ', mut_of_digits(n))
