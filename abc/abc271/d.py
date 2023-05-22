N, S = map(int, input().split())
cards = [0]
for _ in range(N):
    a, b = map(int, input().split())
    cards.append((a, b))

dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True

path = [['']*(S+1) for _ in range(N+1)]

for n in range(1, N+1):
    for s in range(S+1):
        # n=1 の時の処理
        if n==1 and cards[n][0] <= S:
            dp[n][cards[n][0]] = True
            path[n][cards[n][0]] = 'H'
        if n==1 and cards[n][1] <= S:
            dp[n][cards[n][1]] = True
            path[n][cards[n][1]] = 'T'
        # n > 1 の時の処理
        flag1 = False
        flag2 = False
        if s-cards[n][0] >= 0:
            flag1 = True
        if s-cards[n][1] >= 0:
            flag2 = True
        if flag1 and flag2:
            dp[n][s] = dp[n-1][s-cards[n][0]] or dp[n-1][s-cards[n][1]]
            if dp[n-1][s-cards[n][0]]:
                path[n][s] = path[n-1][s-cards[n][0]] + 'H'
            elif dp[n-1][s-cards[n][1]]:
                path[n][s] = path[n-1][s-cards[n][1]] + 'T'
        elif flag1:
            dp[n][s] = dp[n-1][s-cards[n][0]]
            path[n][s] = path[n-1][s-cards[n][0]] + 'H'
        elif flag2:
            dp[n][s] = dp[n-1][s-cards[n][1]]
            path[n][s] = path[n-1][s-cards[n][1]] + 'T'


if dp[N][S]:
    print('Yes')
    print(path[N][S])
else:
    print('No')