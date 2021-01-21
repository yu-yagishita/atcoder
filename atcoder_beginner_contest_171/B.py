n, k = map(int, input().split())
p = list(map(int, input().split()))

ps = sorted(p, reverse=False)[:k]

ans = 0
for i in ps:
    ans += i

print(ans)
