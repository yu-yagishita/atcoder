N, M = [int(_) for _ in input().split()]

A = [int(_) for _ in input().split()]

ans = N
for i in range(M):
    ans -= A[i]

if(ans < 0):
    print("-1")
else:
    print(ans)
