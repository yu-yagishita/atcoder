from collections import deque
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

M = [list(input()) for i in range(R)]

M[sy-1][sx-1] = 0


def bfs(sy, sx):
    queue = deque([(sy, sx)])
    while queue:
        y, x = queue.popleft()
        if M[y-1][x] =='.':
            M[y-1][x] = M[y][x] +1
            queue +=[(y-1, x)]
        if M[y+1][x] =='.':
            M[y+1][x] = M[y][x] +1
            queue +=[(y+1, x)]
        if M[y][x-1] =='.':
            M[y][x-1] = M[y][x] +1
            queue +=[(y, x-1)]
        if M[y][x+1] =='.':
            M[y][x+1] = M[y][x] +1
            queue +=[(y, x+1)]

bfs(sy-1, sx-1)
print(M[gy-1][gx-1])
'''
for row in M:
    print(row)
'''
