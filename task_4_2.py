num = (1, 4, 10, 3, 66, -4, 1)
q = 0
for element in num:
    if element % 2 == 0:
        q += 1
print(f'В списке {q} четных чисел')