fib = [1, 1]
print(type(fib))
for i in range(2, 15):
    fib.append(fib[i-1] + fib[i-2])
print(fib)