n = int(input())
position = []
for i in range(n):
	x_in, l_in = map(int, input().split())
	position.append([x_in + l_in, x_in - l_in])
position.sort()
ans = 0
t = - (10 ** 9 + 1)
for i in range(n):
	if t <= position[i][1]:
		ans += 1
		t = position[i][0]
print(ans)
