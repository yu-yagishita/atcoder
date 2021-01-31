# A 深さ優先探索 再帰関数
import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限

def dfs(v_x, v_y, seen_list, c_list):
    if v_x < 0 or v_y < 0 or v_x >= w or v_y >= h:
        return
    if seen_list[v_y][v_x]:
        return
    if c_list[v_y][v_x] == "#":
        return
    seen_list[v_y][v_x] = True
    dfs(v_x+1,v_y,seen_list,c_list)
    dfs(v_x-1,v_y,seen_list,c_list)
    dfs(v_x,v_y+1,seen_list,c_list)
    dfs(v_x,v_y-1,seen_list,c_list)

h, w = map(int, input().split())
seen_list = [[False] * w for i in range(h)]
c_list = []
s = []
g = []
for i in range(h):
    _tmp = list(input())
    if "s" in _tmp:
        s = [_tmp.index("s"),i]
    if "g" in _tmp:
        g = [_tmp.index("g"),i]
    c_list.append(_tmp)

dfs(s[0],s[1],seen_list,c_list)

if seen_list[g[1]][g[0]]:
    print("Yes")
else:
    print("No")
