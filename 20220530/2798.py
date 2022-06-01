n,m = map(int,input().split())
card = list(map(int,input().split()))
sum = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sam = card[i]+card[j]+card[k]
            if sam <= m:
                sum.append(sam)
print(max(sum))