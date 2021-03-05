MOD = 10**9 + 7
D = int(input())
N = input()
p = [[0] * D for _ in range(2)]
p[0][0] = 1
for i, c in enumerate(N):
    n = int(c)
    q = [[0] * D for _ in range(2)]
    for d in range(D):
        for k in range(10):
            q[1][(d+k)%D] = (q[1][(d+k)%D] + p[1][d]) % MOD
        for k in range(n):
            q[1][(d+k)%D] = (q[1][(d+k)%D] + p[0][d]) % MOD
        q[0][(d+n)%D] = (q[0][(d+n)%D] + p[0][d]) % MOD
    p = q
ans = (p[0][0] + p[1][0] - 1) % MOD
print(ans)
