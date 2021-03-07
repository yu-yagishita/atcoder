N = int(input())
work = [[int(_) for _ in input().split()] for i in range(N)]
A = work[0][0]

onaji = []
for i in range(N):
    onaji.append(work[i][0] + work[i][1])

tigau = []
for j in range(N):
    for k in range(N):
        if not j ==k:
            tigau.append(max(work[j][0], work[k][1]))

print(min(min(tigau), min(onaji)))
