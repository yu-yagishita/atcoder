D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
fuku = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(D)]
for i in range(1, D):
   for j in range(N):
       aj, bj, cj = fuku[j]
       if T[i] < aj or bj < T[i]:
           continue
       for k in range(N):
           ak, bk, ck = fuku[k]
           if T[i - 1] < ak or bk < T[i - 1]:
               continue
           dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(cj - ck))

print(max(dp[-1]))
