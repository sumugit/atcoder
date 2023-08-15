import numpy as np

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

# bit DP
# (2次元の場合) dp[i][S]: i 枚目までのクーポンで買える商品の集合が S であるときの最小枚数
# (1次元の場合) dp[j]: 集合 j の商品が買えるクーポンの最小枚数
dp = [np.inf] * (1 << N)
dp[0] = 0
for i in range(M):
    S = 0 # 集合 (2進数を10進数で表現)
    for j in range(N):
        if A[i][j] == 1:
            S += 1 << j # 集合を整数で表現
    for j in range(1 << N):
        dp[j | S] = min(dp[j | S], dp[j] + 1)

if dp[-1] == np.inf:
    print(-1)
else:
    print(dp[-1])