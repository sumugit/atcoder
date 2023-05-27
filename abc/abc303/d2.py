import numpy as np
X, Y, Z = map(int, input().split())
S = input()

dp = [[np.inf, np.inf] for _ in range(len(S)+1)]
dp[0][0] = 0
cur = 0
for i in range(len(S)):
    if S[i] == 'a':
        cur = 0
    else:
        cur = 1
    # 現在の CapsLock が OFF または ON の状態のとき
    for j in range(2):
        # 次の CapsLock の状態を OFF または ON にする
        for k in range(2):
            v = dp[i][j]
            if j != k:
                v += Z
            if cur == k:
                v += X
            else:
                v += Y
            dp[i+1][k] = min(dp[i+1][k], v)
ans = min(dp[len(S)][0], dp[len(S)][1])
print(ans)
