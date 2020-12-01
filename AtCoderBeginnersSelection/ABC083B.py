N, A, B = [int(_) for _ in input().split()]
total = 0
for i in range(N+1):
    list_i = list(str(i))
    total_digit = 0
    for v in list_i:
        total_digit += int(v)
    if total_digit >= A and total_digit <= B:
        total += i
print(str(total))
