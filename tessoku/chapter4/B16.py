N = int(input())
h = [0] + list(map(int, input().split()))
NUM = 10 ** 5 + 9
COST = 10 ** 4 + 9

dp = [COST] * NUM
dp[1] = 0

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + abs(h[i - 1] - h[i])
    if i > 2:
        dp[i] = min(dp[i], dp[i - 2] + abs(h[i - 2] - h[i]))

print(dp[N])
