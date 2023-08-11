import numpy as np

N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))

dp = [np.inf for _ in range(N+1)]
dp[1] = 0
for i in range(2, N+1):
    if i < 3:
        dp[i] =  min(dp[i], dp[i-1] + A[i])
    else:
        dp[i] = min(dp[i], dp[i-1] + A[i], dp[i-2] + B[i])

print(dp[N])
