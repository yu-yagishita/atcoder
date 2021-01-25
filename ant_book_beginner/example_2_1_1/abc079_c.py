S = input()
space = len(S)-1

for i in range(2**space):
    b = ['-']*space
    for j in range(space):
        if ((i >> j) & 1):
            b[space-1-j] = '+'
    ans = ''
    for k in range(len(b)):
        ans += S[k] + b[k]
    ans += S[3]
    if eval(ans) == 7:
        print(ans + '=7')
        exit(0)
