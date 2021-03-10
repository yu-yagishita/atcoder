MAX_N = 100
MAX_W = 10000

# 入力
N, W = map(int,input().split())

# w = list(map(int,input().split()))
# v = list(map(int,input().split()))
items = [[int(_) for _ in input().split()] for i in range(N)]
dp = [0] * (MAX_W + 1)    # DPテーブル

for i in range(N):
    for j in range(items[i][1], W + 1):
        dp[j] = max(dp[j], dp[j - items[i][1]] + items[i][0])
print(dp[W])
