n, m = map(int, input().split())
dp = [[[0]*102 for _ in range(102)] for _ in range(102)]
for _ in range(n):
    a, b, c, w = map(int, input().split())
    dp[a+1][b+1][c+1] = max(w, dp[a+1][b+1][c+1])

for i in range(1, 102):
    for j in range(1, 102):
        for k in range(1, 102):
            dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k],
                              dp[i][j][k-1], dp[i][j][k])
for _ in range(m):
    x, y, z = map(int, input().split())
    print(dp[x+1][y+1][z+1])
