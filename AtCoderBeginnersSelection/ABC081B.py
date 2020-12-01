N = int(input())
S = [int(_) for _ in input().split()]
total_count = 0
while True:
    even_count = 0
    for i in S:
        if i%2 == 0:
            even_count += 1
    if N == even_count:
        total_count += 1
        for i, val in enumerate(S):
            S[i] = val/2
    else:
        break
print(str(total_count))
