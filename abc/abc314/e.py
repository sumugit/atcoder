N, M = map(int, input().split())
CPS = [list(map(int, input().split())) for _ in range(N)]

# 期待値DP
INF = float('inf')
dp = [INF] * (M + max(max(cps[2:]) for cps in CPS) + 1)
dp[0] = 0

for i in range(1, len(dp)):
    for cps in CPS:
        C, P, S = cps[0], cps[1], cps[2:]
        expected_cost = C / P
        excepted_point = int(sum(S) / P)
        if i - excepted_point >= 0:
            dp[i] = min(dp[i], dp[i - excepted_point] + expected_cost)

print(dp[M])