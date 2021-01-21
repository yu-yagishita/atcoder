import math

n= int(input())
c = [[int(_) for _ in input().split()] for i in range(n)]
ans = 0
d = 0

for i in range(0,n-1):
    for j in range(i,n):
        d = (c[i][0]-c[j][0])**2 + (c[i][1]-c[j][1])**2
        if ans < d:
            ans = d

print(math.sqrt(ans))
