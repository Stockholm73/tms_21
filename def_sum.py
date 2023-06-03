def summ(*args):
    s = False
    testi = ''
    for i in args:
        if type(i) == str:
            s = True
    if s:
        sum_result = ''
        for i in args:
            testi = str(i)
            sum_result = sum_result + testi
    else:
        sum_result = 0
        for i in args:
            sum_result = sum_result + i
    return sum_result


print(summ(1,2,3,4,5))
