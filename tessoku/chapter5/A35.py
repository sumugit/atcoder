N = int(input())
A = list(map(int, input().split()))

dp = [0] + [[0]*i for i in range(1, N+1)]
for i in range(N):
    dp[N][i] = A[i]

for i in range(N-1, 0, -1):
    if i%2 == 1:
        for j in range(i):
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
    else:
        for j in range(i):
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])

print(dp[1][0])