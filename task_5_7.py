def index_max(lis):
    if len(lis) == 0:
        return -1
    m = lis[0]
    index_m = 0
    for i in range(1, len(lis)):
        if lis[i] > m:
            index_m = i
            m = lis[i]
    return index_m


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arr = [[1, 2, 7, 9, 4], [9, 1, 6, 2, 8], [9, 3, 7, 6, 1], [9, 4, 7, 1, 2], [9, 1, 2, 3, 4]]
for i in range(len(arr)):
    k = index_max(arr[i])
    swap(arr[i], i, k)
for i in range(len(arr)):
    print(arr[i])
