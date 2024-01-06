N, K = map(int, input().split())
a = list(map(int, input().split()))

# True → First
# False → Second
dp = [False] * (N+1)
for i in range(N+1):
    for j in range(K):
        if i - a[j] == 0:
            dp[i] = True
            break
        elif i - a[j] > 0 and dp[i-a[j]] == False:
            dp[i] = True
            break

if dp[N]:
    print("First")
else:
    print("Second")