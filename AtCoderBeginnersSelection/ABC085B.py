N = int(input())
d_list = [int(input()) for i in range(N)]
next = 0
total_count = 0
first_max = 0
for i in d_list:
    if first_max < i:
        first_max = i
        kagami_bottom = first_max
total_count += 1
d_list.remove(first_max)

while True:
    if not d_list:
        break
    next_max = 0
    for i in d_list:
        if next_max < i:
            next_max = i
    if kagami_bottom > next_max:
        kagami_bottom = next_max
        total_count += 1
        d_list.remove(next_max)
    elif kagami_bottom == next_max:
        d_list.remove(next_max)

print(total_count)
