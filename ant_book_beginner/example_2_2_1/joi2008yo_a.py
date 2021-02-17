N = int(input())

N = 1000 - N
cnt = 0

l = [500,100,50,10,5,1]

for i in l:
    cnt += N // i
    N = N - i*(N//i)

print(cnt)
