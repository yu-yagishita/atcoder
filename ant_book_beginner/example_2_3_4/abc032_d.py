N,W = map(int,input().split())
vw = [list(map(int,input().split())) for _ in [0]*N]

vM,wM = 0,0
for v,w in vw:
    vM = max(vM,v)
    wM = max(wM,w)

if wM <= 1000: # ➁
    wS = sum(w for v,w in vw)
    if wS <= W:
        ans = sum(v for v,w in vw)
    else:
        dp = [[0]*(W+1) for _ in range(N+1)]
        for i,vw2 in enumerate(vw,1): # イテラブルオブジェクトとインデックスを取得
            v,w = vw2
            for j in range(W+1):
                dp[i][j] = dp[i-1][j]
                if j>=w : dp[i][j] = max(dp[i][j],dp[i-1][j-w] + v)
        ans = dp[-1][W]
    print(ans)
elif vM <= 1000: # ➂
    V = sum(v for v,w in vw)
    dp = [[W+1]*(V+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i,vw2 in enumerate(vw,1):
        v,w = vw2
        for j in range(V+1):
            dp[i][j] = dp[i-1][j]
            if j>=v : dp[i][j] = min(dp[i][j],dp[i-1][j-v]+w)
    print(max(i for i,w in enumerate(dp[-1]) if w<=W))
elif N <= 30: # ➀
  w_max = W
  V,W = zip(*vw) # Weightでソートしたい
  # N <= 30
  # 半分全列挙
  left = [(0,0)] # weight, value
  right = [(0,0)]
  for i in range(N//2):
    left += [(x+W[i],y+V[i]) for x,y in left]
  for i in range(N//2,N):
    right += [(x+W[i],y+V[i]) for x,y in right]
  left.sort() # 重さ順
  right.sort()
  def remove_worthless(li):
    temp = []
    current_value = -1
    for w,v in li:
      if w > w_max:
        break
      # wでの最大値vをリストする
      if v > current_value:
        current_value = v
        temp.append((w,v))
    return temp
  left = remove_worthless(left)
  right = remove_worthless(right)
  INF = 10**18
  right.append((INF,0))
  # double pointer
  j = 0
  x = 0
  for wL,vL in left[::-1]: # leftを逆順
    wR_max = w_max-wL
    while right[j+1][0] <= wR_max:
      j += 1
    vLR = vL + right[j][1]
    if x < vLR:
      x = vLR
  print(x)
