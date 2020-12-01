A = int(input())
B = int(input())
ans = [1, 2, 3]
for i in range(3):
    if A == i:
        ans.remove(i)
    if B == i:
        ans.remove(i)

print(ans[0])
