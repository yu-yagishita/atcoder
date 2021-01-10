K=int(input())
N = [int(_) for _ in input().split()]
A = N[0]
B = N[1]

ans=''
for i in range(A,B+1):
    if i % K == 0:
        ans = 'OK'
if ans != 'OK':
    ans = 'NG'
print(ans)
