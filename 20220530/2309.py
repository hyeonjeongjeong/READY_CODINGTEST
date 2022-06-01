x = [int(input()) for _ in range(9)]
cnt = sum(x) - 100
for j in x:
    if len(x) == 7:
        break
    for k in x:
        if j + k == cnt:
            if j == k:
                continue
            x.remove(j)
            x.remove(k)
            break
        else:
            continue
x.sort()
for v in x:
    print(v)