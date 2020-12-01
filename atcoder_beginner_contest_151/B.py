N, K, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
now_total=0
for i in A:
    now_total += i
last_A= N*M-now_total
if last_A <= 0:
    print(0)
elif last_A <= K and last_A > 0:
    print(last_A)
else:
    print(-1)
