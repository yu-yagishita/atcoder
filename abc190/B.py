N, S, D = map(int, input().split())
jyumon = [[int(_) for _ in input().split()] for i in range(N)]
ans = 0

for i in range(N):
    if jyumon[i][0] >= S or jyumon[i][1] <= D:
        continue
    else:
        ans += 1

if ans > 0:
    print('Yes')
else:
    print('No')
