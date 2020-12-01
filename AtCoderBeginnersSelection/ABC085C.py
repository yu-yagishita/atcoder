N, Y = [int(_) for _ in input().split()]
for x in range(N+1):
    for y in range(N+1):
        z = N - x - y
        total = 10000*x + 5000*y + 1000*z
        if Y == total and 0<= z <= 2000:
            print(x, y, z)
            quit()

print(-1, -1, -1)
