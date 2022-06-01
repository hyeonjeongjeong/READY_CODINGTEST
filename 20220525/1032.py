a = int(input())
b = list(input())
l = len(b)
for _ in range(a-1):
    c = list(input())
    for i in range(l):
        if b[i] != c[i]:
            b[i] = '?'
print(''.join(b))