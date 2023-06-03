def max_of_list(lis):
    maxi = lis[0]
    for element in lis:
        if element > maxi:
            maxi = element
    return maxi


lis = [1, 0, 9, 4, 66, 8, 22, 14, 67, 98, 3, 44, 1, 8, 88, 56, 78, 32, 7]
m = max_of_list(lis)
for i in range(0, len(lis), 2):
    lis[i] = m
print(lis)