def del_double_elem(*args):
    q = 0
    lis = list(args)
    for elem in args:

        if lis.count(elem) > 1:
            while elem in lis:
                lis.remove(elem)

    return lis


print(del_double_elem(1, 2, 3, 1, 2, 3, 'er', 7, 9, 9, 'd', 'd'))
