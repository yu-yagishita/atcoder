# 自分の回答：実行時間エラーがえぐかった

# from math import factorial

# n, a, b = [int(_) for _ in input().split()]
# total = 0
# length = n//2
# for i in range(length):
#     max = n-i
#     r = i+1
#     if not (r == a or r == b):
#         # 小さい値から
#         total += factorial(n) // factorial(r) // factorial(n - r)
#     if not (max == a or max == b):
#         # 大きい値から
#         total += factorial(n) // factorial(max) // factorial(n - max)

# print(total % (10**9 + 7))

M = 10**9 + 7
n, a, b = map(int, input().split())
r = pow(2, n, M) - 1
f = c = 1
for i in range(b):
  f = f * (i + 1) % M
  c = c * (n - i) % M
  if i + 1 == a:
    a = b
    r -= c * pow(f, M - 2, M)
print(r % M)
