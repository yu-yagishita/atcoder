N, M = [int(_) for _ in input().split()]
P = [0 for _ in range(N)]

ans,pen = 0,0
for _ in range(M):
    p,s = input().rstrip().split(' ')
    p = int(p) - 1
    if P[p] == -1:
        continue
    if s == "WA":
        P[p] += 1
    else:
        ans += 1
        pen += P[p]
        P[p] = -1
print(ans,pen)
