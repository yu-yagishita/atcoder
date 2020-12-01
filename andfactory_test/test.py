N=input()
S=N.split(',')
list_num = [int(s) for s in S]
A = []
B=0
for i in range(len(list_num)):
    if i == 0:
        continue
    if (i+1)%2 == 0:
        A.append(list_num[i])
    elif B == list_num[i]:
        A.append(list_num[i])
    B=list_num[i]
print(A)
