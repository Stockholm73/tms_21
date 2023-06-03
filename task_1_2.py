a = int(input())
b = int(input())
if a < 0:
    a = a * -1
if b < 0:
    b = b * -1
result = (a - b)/(1 + (a*b))
print(result)