N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
ans = 0

for i in range(N):
    ans += A[i] * B[i]

if ans == 0:
    print('Yes')
else:
    print('No')
