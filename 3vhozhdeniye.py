lis = (3, 5, 1, 2, 5, 7, 8, 3, 4, 6, 2, 4, 3, 9, 0)
k = 0
res = -1
for i in range(len(lis)):
    if lis[i] == 3:
        k +=1
    if k == 3:
        res = i
        break
print(res)
