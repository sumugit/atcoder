N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))


dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(1, N+1):  # i (>=1) 目までのカードを選ぶ
    for j in range(S+1):  # 和が j (>=0) となる
        # カード i を選ばないか
        x = dp[i-1][j]
        y = False
        if j >= A[i]:
            # カード i を選ぶ
            y = dp[i-1][j-A[i]]
        dp[i][j] = x or y

if dp[N][S]:
    print('Yes')
else:
    print('No')