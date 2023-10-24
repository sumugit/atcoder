N, A, B = map(int, input().split())

def solve(N, A, B):
    dp = [False]*(N+1)  # dp[i]は先手がi個の石に対して勝つかどうか
    for i in range(A, N+1):
        dp[i] = not dp[i-A] or not dp[i-B] if i >= B else not dp[i-A]
    return "First" if dp[N] else "Second"

ans = solve(N, A, B)
print(ans)