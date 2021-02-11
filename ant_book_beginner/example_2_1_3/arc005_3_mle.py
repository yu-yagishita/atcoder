# def bfs()の解法。この書き方だとMLEになってしまう。。
# と思ったら無駄にO(H*W)をしていたせいだった。。
from collections import deque

dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))  # タプルやリストで持っておくと便利
H, W = map(int, input().split())
M = []
s = []
g = []
for i in range(H):
    _tmp = list(input())
    if 's' in _tmp:
        s = [_tmp.index('s'), i]
    if 'g' in _tmp:
        g = [_tmp.index('g'), i]
    M.append(_tmp)


def bfs(sx, sy, gx, gy):
    # 距離＝壁マスを通る回数 として最短路問題を解く。
    dist = [[10**9]*W for i in range(H)]
    dist[sy][sx] = 0
    queue = deque([(sy, sx)])
    while queue:
        y, x = queue.popleft()
        if x == gx and y == gy:  # goalに着いたら終了
            break
        else:
            for dx, dy in dxdy:
                if not ((0 <= x+dx < W) and (0 <= y+dy < H)):
                    continue
                # この経路での始点から遷移先までの距離。壁なら+1
                wall = (M[y][x] == '#')
                d = dist[y][x] + wall

                # 暫定距離より短い経路が得られた場合は更新して、+1なら後ろに、+0なら前に付ける
                if d < dist[y+dy][x+dx]:
                    dist[y+dy][x+dx] = d
                    if wall:
                        queue.append((y+dy, x+dx))
                    else:
                        queue.appendleft((y+dy, x+dx))

    return dist[y][x]


d = bfs(s[0], s[1], g[0], g[1])
# 終点までの距離が2以下ならYES
if d <= 2:
    print('YES')
else:
    print('NO')
