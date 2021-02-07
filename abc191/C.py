h, w = map(int, input().split())
filed = [input() for _ in range(h)]

cnt = 0

for i in range(h-1):
    for j in range(w-1):
        cnt += ((filed[i][j] == '#') + (filed[i+1][j] == '#') +
                (filed[i][j+1] == '#') + (filed[i+1][j+1] == '#')) % 2

print(cnt)
