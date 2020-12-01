N = int(input())
S = input()
R = []
G = []
B = []
for i in range(N):
    if S[i] == 'R':
        R.append(i)
    elif S[i] == 'G':
        G.append(i)
    elif S[i] == 'B':
        B.append(i)
ans = len(R)*len(G)*len(B)
for i in range(1,(N+1)//2):
    for j in range(i,N-i):
        if S[j] != S[j-i] and S[j] != S[j+i] and S[j-i] != S[j+i]:
            ans -= 1
print(ans)
