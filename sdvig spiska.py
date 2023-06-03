def sdvig(lis):
    if len(lis) > 2:
        t = lis[0]
        for i in range(len(lis) - 1):
            lis[i] = lis[i + 1]
        lis[-1] = t


l = [1, 2, 3, 4, 5, 6]
sdvig(l)
print(l)