A,B,K = [int(_) for _ in input().split()]
if K <= A:
    A -= K
elif K <= A+B:
    B -= K-A
    A = 0
elif A+B < K:
    A = 0
    B = 0
print(A, B)
