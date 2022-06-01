a = input()
b = ''
for i in a:
    if i in 'ABC':
        b += chr(ord(i) +23)
    else:
        b += chr(ord(i) - 3)
print(b)