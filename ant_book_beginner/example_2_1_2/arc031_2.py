import sys
import copy
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限

def dfs(v_x, v_y, seen_list, c_list, island_area_count):
    if v_x < 0 or v_y < 0 or v_x >= w or v_y >= h:
        return
    if seen_list[v_x][v_y]:
        return
    if c_list[v_x][v_y] == "x":
        return
    seen_list[v_x][v_y] = True
    island_area_count[0] += 1
    dfs(v_x+1,v_y,seen_list,c_list,island_area_count)
    dfs(v_x-1,v_y,seen_list,c_list,island_area_count)
    dfs(v_x,v_y+1,seen_list,c_list,island_area_count)
    dfs(v_x,v_y-1,seen_list,c_list,island_area_count)

h, w = 10, 10
island_area = 0
c_list = []
s = []
# inputの整理
for i in range(h):
    _tmp = list(input())
    c_list.append(_tmp)

# 島のマス数を調べる
for j in range(h):
    for k in range(w):
        if c_list[j][k] == 'o':
            island_area += 1
        if not s and c_list[j][k] == 'o':
            s = [j, k]

if island_area == 0:
    print('NO')
    exit(0)

initial_area_count = [0]
initial_seen_list = [[False] * w for i in range(h)]
dfs(s[0],s[1],initial_seen_list,c_list,initial_area_count)
if initial_area_count[0] == island_area:
    print("YES")
    exit(0)

# 埋立地の仮で設定して全島のマスを探索できるか調べる
for l in range(h):
    for m in range(w):
        kari_list =copy.deepcopy(c_list)
        seen_list = [[False] * w for i in range(h)]
        island_area_count = [0]
        if c_list[l][m] == 'x':
            kari_list[l][m] = 'o'
            dfs(s[0],s[1],seen_list,kari_list, island_area_count)
            if island_area_count[0] == island_area + 1:
                print('YES')
                exit(0)
print('NO')
