def sum_of_divisor(number):
    result = 0
    for i in range(1, number):
        if number % i == 0:
            result += i
    return result


def if_friend(a, b):
    if sum_of_divisor(a) == b and sum_of_divisor(b) == a:
        return True
    else:
        return False


ans1 = []
ans2 = []
for i in range(200, 301):
    for j in range(200, 301):
        if if_friend(i, j):
            ans1.append(i)
            ans2.append(j)
for i in range(len(ans1)):
    print(f'{ans1[i]} {ans2[i]}')

