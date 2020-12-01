N, A = [int(_) for _ in input().split()]
count = 0
while True:
    if N > 0:
        N -= A
        count += 1
    else:
        break

print(count)
