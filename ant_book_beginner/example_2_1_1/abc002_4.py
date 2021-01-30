import itertools

N, M = map(int, input().split())
# * tupleにしているのはitertools.combinetaionsを使うため
XY = [tuple(map(int, input().split())) for _ in range(M)]
# * setで重複を消す必要はないかも。
XY = set(XY)
ans = 1

for i in range(2**N):
    S = []
    for j in range(N):
        if (i >> j) & 1:
            # * グループに入る議員さんの人数を全パターンで出している
            S.append(j+1)
    # * 組み合わせを求めている
    S_comb = itertools.combinations(S, 2)
    flag = True
    for pair in S_comb:
        if pair in XY:
            continue
        else:
            # * グループの議員さんが全員知り合いではなかった場合
            flag = False
            break
    if flag:
        ans = max(len(S),ans)

print(ans)
