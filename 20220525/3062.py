a = int(input())
for i in range(a):
    n = input()
    m = ''
    for j in n:
        m = j + m
    num = str(int(n) + int(m))
    for k in range(len(str(num)) // 2):
        if num[k] != num[-(k+1)]:
            print('NO')
            break
    else:   
        print('YES')