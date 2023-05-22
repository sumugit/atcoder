from collections import defaultdict

N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = defaultdict(int)
for _ in range(M):
    c, y = map(int, input().split())
    Y[c] = y

dp = [[0 for _i in range(N+1)] for _j in range(N+1)]
# コイントス回数
for i in range(1, N+1):
    # カウンタ
    for j in range(1, i+1):
        dp[i][j] = dp[i-1][j-1] + X[i-1] + Y[j]
        dp[i][0] = max(dp[i][0], dp[i-1][j])

print(max(dp[N]))