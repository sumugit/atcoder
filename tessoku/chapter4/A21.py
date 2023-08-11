N = int(input())
PA = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)] + [[0, 0]]

# 区間 DP
# dp[l][r]: 区間[l, r]の最大得点
dp = [[0] * (N+1) for _ in range(N+1)]
for length in range(N-2, -1, -1):
    for i in range(1, N-length+1):
        j = i + length
        score1 = score2 = 0
        if i <= PA[i-1][0] <= j:
            score1 = PA[i-1][1]
        if i <= PA[j+1][0] <= j:
            score2 = PA[j+1][1]
        
        if i == 1:
            dp[i][j] = dp[i][j+1] + score2
        elif j == N:
            dp[i][j] = dp[i-1][j] + score1
        else:
            dp[i][j] = max(dp[i-1][j]+score1, dp[i][j+1]+score2)

ans = max(dp[i][i] for i in range(1, N+1))
print(ans)