N = int(input())
X = [int(_) for _ in input().split()]
max = 0
min = 100
for i in X:
    if max < i:
        max = i
    if min > i:
        min = i

ans = 0
for p in range(max-min):
    total = 0
    for i in X:
        total += (i-p) ** 2
    if ans == 0:
        ans = total
    if ans > total:
        ans = total
print(ans)
