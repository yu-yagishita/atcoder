from itertools import accumulate, product, permutations, combinations

N = int(input())
l = [i+1 for i in range(N)]
c_list = list(permutations(l))
P = tuple(int(_) for _ in input().split())
Q = tuple(int(_) for _ in input().split())
P_value = 0
Q_value = 0
for index, item in enumerate(c_list):
    if P == item:
        P_value = index+1
    if Q == item:
        Q_value = index+1

print(abs(P_value - Q_value))
