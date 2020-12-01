N = int(input())

maxcnt = 0
ixy = []

for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        ixy.append([i, x - 1, y])

# print(ixy)

# bit全探索
for bit in range((1 << N)):
    # 2重ループがうまく抜けられない...
    break_flag = False
    for i, x, y in ixy:
        # 対応するbitが1のとき正直者、0のとき嘘つき
        # 正直者iの証言が
        if ((bit >> i) & 1):
            # bitの状態と一致しないとき矛盾
            if ((bit >> x) & 1 != y):
                break_flag = True
                # print("break1", i, x, y)
                break
    # 嘘つきは反対の証言になるわけではなく真偽不明として無視するらしい...
    # breakしてきたときはカウントしない
    if break_flag:
        continue
    # ここまで全て矛盾がなければ立っているbitの数 (= 正直者の数) をカウント
    # 最大値を更新
    else:
        # print(bin(bit))
        maxcnt = max(maxcnt, bin(bit).count("1"))

print(maxcnt)
