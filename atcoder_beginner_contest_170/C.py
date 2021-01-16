x, n = map(int, input().split())
p = list(map(int, input().split()))

for i in range(x+1):
    for j in [-1, +1]:
        a = x+i*j
        if p.count(a) == 0:
            print(a)
            exit(0)
