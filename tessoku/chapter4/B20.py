S = input()
T = input()

# SとTが一致するための編集距離
# dp[i][j] = Sのi文字目までとTのj文字目までの編集距離
dp = [[0 for j in range(len(T)+1)] for i in range(len(S)+1)]

for i in range(len(S)+1):
    for j in range(len(T)+1):
        if i == 0 or j == 0:
            dp[i][j] = i + j
        elif S[i-1] == T[j-1]:
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]) # 削除、挿入、一致
        else:
            dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1) # 削除、挿入、置換

print(dp[len(S)][len(T)])