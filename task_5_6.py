lis = [2, 3, 4, 1, 6, 8, 10, 65, 4, 3, 2, 7, 8, 2, 6, 8, 9, 1, 2, 3, 4, 3, 4, 5, 6, 11]
lis_start = []
lis_finish = []
if_inside = False
for i in range(len(lis) - 1):
    if not if_inside:
        if lis[i + 1] > lis[i]:
            lis_start.append(i)
            if_inside = True
    else:
        if lis[i + 1] <= lis[i]:
            lis_finish.append(i)
            if_inside = False
if len(lis_start) != len(lis_finish):
    lis_finish.append(len(lis) - 1)
print(len(lis_start))
