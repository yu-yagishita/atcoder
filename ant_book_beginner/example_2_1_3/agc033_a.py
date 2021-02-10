from collections import deque

dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))  # タプルやリストで持っておくと便利
H, W = map(int, input().split())
M = []
dist = [[-1]*W for _ in range(H)]
black_cells = deque()
for i in range(H):
    _tmp = list(input())
    for j in range(W):
        if _tmp[j] == '#':
            black_cells.append((i, j))
            dist[i][j] = 0
    M.append(_tmp)


def bfs(queue):
    while queue:
        y, x = queue.popleft()
        for dx, dy in dxdy:
            # 見訪問かつ通行可能か
            if (0 <= x+dx < W) and (0 <= y+dy < H) and dist[y+dy][x+dx] == -1 and M[y+dy][x+dx] != '#':
                queue += [(y+dy, x+dx)]
                dist[y+dy][x+dx] = dist[y][x] + 1  # 距離を記録

    return dist[y][x]


d = bfs(black_cells)
print(d)
