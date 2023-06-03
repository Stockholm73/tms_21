lis = [11, 1, 1, 1, 2, 2, 10, 12, 12, 12, 11, 2, 3, 3, 3, 4, 5, 5, 1, 2, 3]
# testlist = "",
lis1 = list()
for el in lis:
    if lis1.count(el) == 0:
        lis1.append(el)
print(lis1)
print(lis)
