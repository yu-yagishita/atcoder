import itertools

n = int(input())
k = int(input())

cards = []
for i in range(n):
    c = map(str, input().split())
    cards += c
ans = 0
ans_list = []

# 頂点を並び替える順列を生成してループ
for i in itertools.permutations(range(n), k):
    tmp = ''
    for j in range(len(i)):
        tmp += cards[i[j]]
    if not tmp in ans_list:
        ans_list.append(tmp)
        ans += 1

print(ans)
