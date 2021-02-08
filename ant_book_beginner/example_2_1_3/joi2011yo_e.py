from collections import deque

dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))  # タプルやリストで持っておくと便利
H, W, N = map(int, input().split())
M = []
s = []
ans = 0
for i in range(H):
    _tmp = list(input())
    if "S" in _tmp:
        s = [_tmp.index("S"), i]
    M.append(_tmp)


def bfs(sx, sy, g):
    dist = [[-1]*W for _ in range(H)]
    dist[sy][sx] = 0
    queue = deque([(sy, sx)])
    while queue:
        y, x = queue.popleft()
        if M[y][x] == g:  # * goalに着いたら終了
            break
        else:
            for dx, dy in dxdy:
                # 見訪問かつ通行可能か
                if (0 <= x+dx < W) and (0 <= y+dy < H) and dist[y+dy][x+dx] == -1 and M[y+dy][x+dx] != 'X':
                    queue += [(y+dy, x+dx)]
                    dist[y+dy][x+dx] = dist[y][x] + 1  # 距離を記録
    s[0] = x
    s[1] = y
    return dist[y][x]


for n in range(1, N+1):
    d = bfs(s[0], s[1], str(n))
    ans += d
print(ans)
