N = int(input())
A = [int(_) for _ in input().split()]

N_map = {}

for i in range(1, N+1):
    N_map[i] = 0

for i in A:
    if i in N_map:
        N_map[i] += 1

for i in N_map.values():
    print(i)
