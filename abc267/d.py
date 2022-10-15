N, M = map(int, input().split())
A = [0] + list(map(int, input().split())) # A の index も N に揃える. (DP ではよく使う)


dp = [[-1000000000000000000]*(M+1) for _ in range(N+1)]  # 和が負になる可能性があることに注意
dp[0][0] = 0
for n in range(1, N+1):
    for m in range(0, M+1):
        if m == 0:
            dp[n][m] = 0
        elif m <= n:
            temp1 = dp[n-1][m]
            temp2 = dp[n-1][m-1] + m*A[n]
            dp[n][m] = max(temp1, temp2)

print(dp[N][M])

