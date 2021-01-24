import sys
input = sys.stdin.readline

n, x = map(int, input().split())
k = [[int(_) for _ in input().split()] for i in range(n)]

ans = 0

x *= 100

for i in range(n):
    x -= k[i][0]*k[i][1]
    ans += 1
    if x<0:
        print(ans)
        exit(0)


print(-1)
