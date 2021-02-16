import itertools

N = int(input())

A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
count = 0
a_win_count = 0
for a in itertools.permutations(A, N):
    for b in itertools.permutations(B, N):
        count += 1
        a_score = 0
        b_score = 0
        for i in range(N):
            if a[i] > b[i]:
                a_score += 1
            elif a[i] < b[i]:
                b_score += 1
        if a_score > b_score:
            a_win_count += 1

print(a_win_count/count)
