N = int(input())
t = [int(input()) for i in range(N)]
ans = []

for i in range(2**N):
    b = [0]*N
    for j in range(N):
        if ((i >> j) & 1):
            b[N-1-j] = 1
    nikuyaki_0 = 0
    nikuyaki_1 = 0
    for k in range(len(b)):
        if b[k] == 0:
            nikuyaki_0 += t[k]
        else:
            nikuyaki_1 += t[k]
    if nikuyaki_0>nikuyaki_1:
        ans.append(nikuyaki_0)
    else:
        ans.append(nikuyaki_1)

print(min(ans))
