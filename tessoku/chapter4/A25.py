H, W = map(int, input().split())
C = [list(input().split()) for _ in range(H)]
C = [[char for char in inner_list[0]] for inner_list in C]

# dp[i][j]: マス (i, j) に移動する通り数
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        if C[i][j] == "#":
            continue
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]
ans = dp[-1][-1]
print(ans)