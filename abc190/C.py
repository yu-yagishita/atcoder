N, M = map(int, input().split())
condition = [[int(_) for _ in input().split()] for i in range(M)]
K = int(input())
choice = [[int(_) for _ in input().split()] for i in range(K)]
ans = 0

for i in range(2**K):
    b = [0]*(N)
    for j in range(K):
        if ((i >> j) & 1):
            b[choice[j][0]-1] = 1
        else:
            b[choice[j][1]-1] = 1
    p = 0
    for l in range(M):
        if b[condition[l][0]-1] == 0:
            continue
        if b[condition[l][1]-1] == 0:
            continue
        p += 1
        if p > ans:
            ans = p

print(ans)
