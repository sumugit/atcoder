N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[False for j in range(S+1)] for i in range(N+1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        if j >= A[i]:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i]]
        else:
            dp[i][j] = dp[i - 1][j]

if dp[N][S]:
    trace = []
    i = N
    rest = S
    while rest > 0:
        if dp[i-1][rest]:
            i -= 1
        else:
            trace.append(i)
            rest -= A[i]
    print(len(trace))
    print(*trace[::-1])
else:
    print(-1)