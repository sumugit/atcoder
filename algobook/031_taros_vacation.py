N = int(input())
A = [0] + list(map(int, input().split()))

dp = [0 for _ in range(N+1)]
dp[1] = A[1]
for i in range(2, N+1):
    dp[i] = max(dp[i-1], dp[i-2]+A[i])

print(dp[N])