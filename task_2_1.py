string = input("Input string: ")
sym3 = string[2]
predpos = string[-2]
first5 = string[:5]
del2 = string[:-2]
et = ''
for i in range(0, len(string), 2):
    et=et + string[i]
print(string, sym3, predpos, first5, del2,et)