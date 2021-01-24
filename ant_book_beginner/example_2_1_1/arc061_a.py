S = input()
space = len(S)-1
s_list = S.split() 
ans = 0

for i in range(2**space):
    b = [0]*space
    f = S[0]
    for j in range(space):
        if ((i >> j) & 1):
            b[space-1-j] = 1
            f += "+"
        f += S[j+1]
    dd = list(map(int, f.split("+")))
    ans += sum(map(int, f.split("+")))

print(ans)
