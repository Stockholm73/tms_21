def hello(name):
    return f'Hello, {name}'


names = []
for i in range(5):
    names.append(input('Input name '))
for name in names:
    print(hello(name))
