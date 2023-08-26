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
    Z_per_XY.append((z/(x+y), i))
Z_per_XY_sorted = sorted(Z_per_XY, reverse=True, key=lambda x: x[0])

print(takahashi_side, aoki_side)
print(Z_per_XY_sorted)

if takahashi_side > sum_z//2:
    print(0)
else:
    # ans = 0
    # for i in range(len(Z_per_XY_sorted)):
    #     z, j = Z_per_XY_sorted[i]
    #     x, y, z = XYZ[j]
    #     if x > y:
    #         continue
    #     else:
    #         takahashi_side += z
    #         aoki_side -= z
    #         if takahashi_side > sum_z//2:
    #             ans += (y-x+1)//2
    #             break
    #         ans += (y-x+1)//2
    # print(ans)
    # DP で解く
    # dp[i][j] : ??
    dp = [[1e+9]*(sum_z) for _ in range(N+1)]
    for i in range(N):
        z, j = Z_per_XY_sorted[i]
        x, y, z = XYZ[j]            
        for j in range(sum_z):
            if x > y:
                dp[i+1][j] = dp[i][j]
            else:
                if j < z:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = min(dp[i][j], dp[i][j-z] + (y-x+1)//2)
    print(dp[N][sum_z//2])