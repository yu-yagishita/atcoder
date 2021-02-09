from collections import deque

dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))  # タプルやリストで持っておくと便利
H, W = map(int, input().split())
M = []
start_black_masu = 0
s = [0, 0]
for i in range(H):
    _tmp = list(input())
    for j in range(W):
        if _tmp[j] == '#':
            start_black_masu += 1
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
                if (0 <= x+dx < W) and (0 <= y+dy < H) and dist[y+dy][x+dx] == -1 and M[y+dy][x+dx] != '#':
                    queue += [(y+dy, x+dx)]
                    dist[y+dy][x+dx] = dist[y][x] + 1  # 距離を記録

    s[0] = x
    s[1] = y
    if M[y][x] != g:
        return -1
    else:
        return dist[y][x]


M[H-1][W-1] = 'G'
d = bfs(s[0], s[1], M[H-1][W-1])
if d == -1:
    print(d)
else:
    ans = (H*W) - (d+1) - start_black_masu
    print(ans)
