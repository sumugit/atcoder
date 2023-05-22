N, K, D = map(int, input().split())
A = list(map(int, input().split()))
# 3 次元 DP で考える
# dp[i][j][k] : i 番目までの要素の中から j 個取り出した時の和を D で割った余りがkとなる
dp = []
for i in range(N+1):
    elem = [[-1]*D for _ in range(K+1)]
    dp.append(elem)
dp[0][0][0] = 0
for i in range(N):
    for j in range(K+1):
        for k in range(D):
            if dp[i][j][k] == -1: continue
            # ai を選ばない時
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
            if j != K:
                # ai を選ぶ時
                dp[i+1][j+1][(dp[i][j][k]+A[i])%D] = max(dp[i+1][j+1][(dp[i][j][k]+A[i])%D], dp[i][j][k] + A[i])
print(dp[N][K][0])
