S = list(input())
T = list(input())
flag = False
for i in reversed(range(len(S) - len(T) + 1)):
    T_flg = S[i: i + len(T)]
    for j in range(len(T)):
        if T_flg[j] != T[j] and T_flg[j] != "?":
            break
    else:
        flag = True
        S[i:i + len(T)] = T
        break
if flag == False:
    print("UNRESTORABLE")
else:
    print("".join(map(str, S)).replace('?', 'a'))
