N = int(input())
w = [[int(_) for _ in input().split()] for i in range(N)]

floor = [w[0]]

for i in range(1, N):
    for j in range(len(floor)):
        if floor[j] >= w[i]:
            floor[j] = w[i]
            break
    else:
        floor.append(w[i])

print(len(floor))
