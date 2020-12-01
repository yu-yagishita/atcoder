S = input()
rev_S = S[::-1]
length = len(S)//2
count = 0

for i in range(length):
    if S[i] != rev_S[i]:
        count +=1

print(count)
