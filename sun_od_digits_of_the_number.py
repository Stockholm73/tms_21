from functools import reduce

num = 28348928374
n = list(str(num))

result = reduce(lambda a, x: int(a) + int(x), n)
print(result)