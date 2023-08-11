N, W = map(int, input().split())
wv = [-1] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for j in range(W+1)] for i in range(N+1)]

for i in range(1, N+1):
    for j in range(W+1):
        w, v = wv[i]
        if j-w >= 0:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][W])