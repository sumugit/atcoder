N = int(input())
TXA = [list(map(int, input().split())) for _ in range(N)]
A = [[0]*5 for _ in range(TXA[N-1][0]+1)]
for i in range(N):
    A[TXA[i][0]][TXA[i][1]] = TXA[i][2]

dp = [[0]*5 for _ in range(TXA[N-1][0]+1)]
now = 0
move_lst = [[0]*5 for _ in range(TXA[N-1][0]+1)]
move_lst[0][0] = 1
for t in range(1, TXA[N-1][0]+1):
    for n in range(5):
        dp0 = 0
        dp1 = 0
        dp2 = 0
        if n > 0 and move_lst[t-1][n-1] == 1:
            dp0 = dp[t-1][n-1] + A[t][n]
            move_lst[t][n] = 1
        if n < 4 and move_lst[t-1][n+1] == 1:
            dp1 = dp[t-1][n+1] + A[t][n]
            move_lst[t][n] = 1
        if move_lst[t-1][n] == 1:
            dp2 = dp[t-1][n] + A[t][n]
            move_lst[t][n] = 1
        dp[t][n] = max(dp0, dp1, dp2)
        
print(max(dp[TXA[N-1][0]]))