# D, G = map(int, input().split())
# A = [[int(_) for _ in input().split()] for i in range(D)]
# hantei = D
# ans = 0
# for i in range(len(A)):
#     ans += A[i][0]

# for i in range(2**hantei):
#     b = [0]*hantei
#     for j in range(hantei):
#         if ((i >> j) & 1):
#             b[hantei-1-j] = 1
#     for k in range(len(b)):
#         tensu = 0
#         if b[k]==1:
#             tensu += (k+1)*100*A[k][0]+A[k][1]
#         if tensu>=G and ans>A[k][0]:
#             ans = A[k][0]
# print(ans)

D, G = map(int, input().split())
G //= 100
l = []
for i in range(D):
  p, c = map(int, input().split())
  tmp = [i+1, p, (i+1)*p+(c//100)]
  l.append(tmp)

ans = []
for i in range(2**D):
  tmp, cnt = 0, 0
  flag = True
  for j in range(D):
    if (i>>j) & 1:
      tmp += l[-j-1][2]
      cnt += l[-j-1][1]
    else:
      if flag:
        mx = D-j
        flag = False
  if tmp >= G:
    ans.append(cnt)
  elif tmp+mx*(l[mx-1][1]-1) >= G:
    cnt += (G-tmp) // mx
    if (G-tmp) % mx != 0:
      cnt += 1
    ans.append(cnt)
print(min(ans))
