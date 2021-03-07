N = int(input())
A = list(map(int, input().split()))
ans_1 = 0
ans_2 = 0
for i in range(N):
    ans_1 += A[i]**2
    ans_2 += A[i]
 
print(N*ans_1 - (ans_2)**2)
