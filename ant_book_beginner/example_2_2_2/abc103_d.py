N, M = map(int, input().split())
position = []

for i in range(M):
    a, b = map(int, input().split())
    position.append([b, a])

position.sort()
ans = 0
t = - (10 ** 9 + 1)

for i in range(M):
    if t <= position[i][1]:
        ans += 1
        t = position[i][0]

print(ans)

# n, m = map(int, input().split())
# ba = []
# for i in range(m):
#     ba.append(list(map(int, input().split())))
#     ba[i][0], ba[i][1] = ba[i][1] - 1, ba[i][0] - 1
# ba.sort()
# bridge = [ba[0][0] - 1]
# for i in range(1, m):
#     if ba[i][1] > bridge[-1]:
#         bridge.append(ba[i][0] - 1)
# print(len(bridge))
# 
