N, W = map(int, input().split())
wv = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

max_value = sum(v for w, v in wv)
dp = [[float('inf')] * (max_value + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    w, v = wv[i]
    for j in range(max_value + 1):
        if j - v >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v] + w)
        else:
            dp[i][j] = dp[i - 1][j]

# 重さの条件満たすかどうかは最後！
ans = max(j for j in range(max_value + 1) if dp[N][j] <= W)
print(ans)
