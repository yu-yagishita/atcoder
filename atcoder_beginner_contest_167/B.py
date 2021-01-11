# N = [int(_) for _ in input().split()]
A, B, C, K = map(int, input().split())
ans = 0
# for i in range(K):
#     if A > 0:
#         A -= 1
#         ans += 1
#         continue
#     if B > 0:
#         B -= 1
#         ans += 0
#         continue
#     if C > 0:
#         C -= 1
#         ans += -1
#         continue

xa = min(A, K)
K -= xa

xb = min(B, K)
K -= xb

xc = K

ans = xa - xc
print(ans)
