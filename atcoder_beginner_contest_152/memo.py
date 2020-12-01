# a問題
L, R = map(int,input().split())

if L == R:
    print("Yes")
else:
    print("No")

# b問題
L, R = map(int,input().split())
l = str(L)
r = str(R)
last_l = ""
last_r = ""
for i in range(L):
    last_r += r
for i in range(R):
    last_l += l
if L > R:
    print(last_r)
else:
    print(last_l)


# c問題
fast_list = list(map(int, input().split()))
correct_answer_count = 0
for i in range(1, fast_list[0] + 1):
    bat_answer_count = 0
    for j in range(1, i+1):
        if not (fast_list[1][i] <= fast_list[1][j]):
            bat_answer_count += 1

    if bat_answer_count == 0:
        correct_answer_count += 1

print(correct_answer_count)

N = int(input())
A = list(map(int, input().split()))
correct_answer_count = 0
for i in range(N):
    bat_answer_count = 0
    for j in range(i):
        if len(A) < j:
            continue
        if not (A[i] <= A[j]):
            bat_answer_count += 1

    if bat_answer_count == 0:
        correct_answer_count += 1

print(correct_answer_count)
