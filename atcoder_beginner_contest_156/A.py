N, R = [int(_) for _ in input().split()]
ans = 0
if N < 10:
    ans = R + (100 * (10 - N))
else:
    ans = R
print(ans)
