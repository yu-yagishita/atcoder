# pypyなら通った
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

K = int(input())
ans = 0
for i in range(K):
    for j in range(K):
        for k in range(K):
            ans += gcd(i+1, j+1, k+1)

print(ans)
