n, m = map(int, input().split())
c = [ int(x) for x in input().split() ]

dp = [ float('inf') ] * 50001
dp[0] = 0

for i in range(50001):
    for j in c:
        if i+j > 50000:
            continue
        else:
            dp[i+j] = min(dp[i+j], dp[i]+1)

print (dp[n])
