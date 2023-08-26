N = int(input())
XYZ = [list(map(int, input().split())) for _ in range(N)]

takahashi_side = 0
aoki_side = 0
sum_z = 0
Z_per_XY = []
for i in range(len(XYZ)):
    x, y, z = XYZ[i]
    if x > y:
        takahashi_side += z
    else:
        aoki_side += z
    sum_z += z

if takahashi_side > sum_z//2:
    print(0)
else:
    # dp[n]: ちょうどn議席得られるのに必要な鞍変えする人の最小値 (ちょうどn議席得られることがありえない場合は無限)
    dp = [1e+20]*(sum_z+1)
    dp[0] = 0
    for i in range(N):
        x, y, z = XYZ[i]
        # 逆から更新することで, 重複を防ぐ
        for j in range(sum_z, z-1, -1):
            if x > y:
                # コスト0で議席を獲得できる
                temp = 0
            else:
                temp = (y-x+1)//2
            dp[j] = min(dp[j], dp[j-z] + temp)
    ans = 1e+20
    for i in range(sum_z//2+1, sum_z+1):
        ans = min(ans, dp[i])
    print(ans)