dic = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dic1 = {}
for k in dic:
    dic1[k + str(len(k))] = dic[k]
dic = dic1
print(dic)