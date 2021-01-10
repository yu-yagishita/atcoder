N, K = map(int, input().split())
s = [1] * N
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for j in range(d):
        s[A[j]-1] = 0
print(sum(s))
