import sys
sys.setrecursionlimit(10**7)


def dfs(v_x, v_y, seen_list, c_list):
    if v_x < 0 or v_y < 0 or v_x >= w or v_y >= h:
        return
    if seen_list[v_y][v_x]:
        return
    if c_list[v_y][v_x] == 0:
        return
    seen_list[v_y][v_x] = True
    dfs(v_x+1, v_y, seen_list, c_list)
    dfs(v_x-1, v_y, seen_list, c_list)
    dfs(v_x, v_y+1, seen_list, c_list)
    dfs(v_x, v_y-1, seen_list, c_list)


w, h = map(int, input().split())
seen_list = [[False] * w for i in range(h)]
c_list = []
s = []
ans = 0
for i in range(h):
    _tmp = list(map(int, input().split()))
    if "s" in _tmp:
        s = [_tmp.index("s"), i]
    c_list.append(_tmp)

for i in range(w):
    for j in range(h):
        if seen_list[j][i] == False and c_list[j][i] == 0:
            seen_list[j][i] = True
        elif seen_list[j][i] == False and c_list[j][i] == 1:
            # * dfsのロジックが(x, y, ...)の順番で欲しかった。
            s = [i, j]
            dfs(s[0], s[1], seen_list, c_list)
            ans += 1

print(ans)
