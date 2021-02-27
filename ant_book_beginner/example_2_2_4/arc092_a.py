from operator import itemgetter

N = int(input())
red = [[int(_) for _ in input().split()] for i in range(N)]
blue = [[int(_) for _ in input().split()] for i in range(N)]

r_sort = sorted(red, key=itemgetter(1), reverse=True)
b_sort = sorted(blue)
ans = 0
r_flag = [False]*N
b_flag = [False]*N

for i in range(len(b_sort)):
    for j in range(len(r_sort)):
        if r_sort[j][0] < b_sort[i][0] and r_sort[j][1] < b_sort[i][1] and r_flag[j] == False and b_flag[i] == False:
            ans += 1
            r_flag[j] = True
            b_flag[i] = True


print(ans)
