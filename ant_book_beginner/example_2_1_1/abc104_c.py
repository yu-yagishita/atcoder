D, G = map(int, input().split())
G //= 100
l = []
for i in range(D):
    p, c = map(int, input().split())
    tmp = [i+1, p, (i+1)*p+(c//100)]
    l.append(tmp)

ans = []

# * これがbit探索を表現している
for i in range(2**D):
    tmp, cnt = 0, 0
    flag = True
    for j in range(D):
        if (i >> j) & 1:
            # * 全問正解したときの値を設定している。
            # * tmp:得点, cnt:問題数
            tmp += l[-j-1][2]
            cnt += l[-j-1][1]
        else:
            if flag:
                # * 全問正解ではなくGに達するために点数が低い問題に取り組んでいる際の何点問題に取り組んでいるかを表している
                mx = D-j
                flag = False
    # * 全問正解でGを超えるかどうか
    if tmp >= G:
        ans.append(cnt)
    # * 中途半端に問題を解いてGを超えるかどうか
    elif tmp+mx*(l[mx-1][1]-1) >= G:
        cnt += (G-tmp) // mx
        if (G-tmp) % mx != 0:
            cnt += 1
        ans.append(cnt)
print(min(ans))
