# import numpy as np
N = int(input())
a = list(map(int, input().split()))

# DP
ans = 0
for i in range(1, N+1):
    #dp = np.zeros(shape=(N+1, i+1, i+1), dtype=int)
    dp = [[[0 for k in range(i+1)] for j in range(i+1)] for _i in range(N+1)]
    #dp[0, 0, 0] = 1
    dp[0][0][0] = 1
    for j in range(0, N):
        for k in range(0, i+1):
            for l in range(0, i):
                # ここで実装するのは現在から見て次のステップ
                dp[j + 1][k][l] += dp[j][k][l]
                if k != i: dp[j + 1][k + 1][(l + a[j])%i] += dp[j][k][l]  # 末端に到達したら次のステップが存在しないことに注意
    ans += dp[N][i][0]

print(ans%998244353)