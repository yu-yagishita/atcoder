a,b = [int(i) for i in input().split()]
l  = [int(i) for i in input().split()]
l.append(l[0] + a)

l2 = [l[i+1] - l[i] for i in range(b)]

print(a - max(l2))
