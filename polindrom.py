string = input('input word')
string1 = string[::-1]
if string == string1:
    print(f'{string} is palindrome')
else:
    print(f'{string} is not palindrome')