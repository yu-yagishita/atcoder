H, N = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
for i in A:
    if H > 0:
        H -= i
if H <= 0:
    print("Yes")
else:
    print("No")
