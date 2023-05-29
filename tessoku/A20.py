S = input()
T = input()

# 最長共通部分列問題
dp = [[0 for j in range(len(T)+1)] for i in range(len(S)+1)]

for i in range(len(S)+1):
    for j in range(len(T)+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif S[i-1] == T[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(S)][len(T)])
