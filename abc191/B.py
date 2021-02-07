N, X = map(int, input().split())
A = list(map(int, input().split()))
ans_list = []
ans = ''

while A:
    a = A.pop()
    if not a == X:
        ans_list.append(str(a))

ans_list.reverse()
ans = ' '.join(ans_list)
print(ans)

# * 別解
n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = [e for e in a if e != x]

print(*ans)
