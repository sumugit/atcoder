N, S = map(int, input().split())
A = [-1] + list(map(int, input().split()))

dp = [[False for j in range(S+1)] for i in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(S+1):
        if j-A[i] >= 0:
            dp[i][j] = dp[i-1][j] | dp[i-1][j-A[i]]
        else:
            dp[i][j] = dp[i-1][j]
                
# for i in range(1, N+1):
#     print(dp[i])

if dp[N][S]:
    print("Yes")
else:
    print("No")