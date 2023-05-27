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

# 最適経路は逆順からたどる
ans = []
i = N
while i > 0:
    if i == N:
        ans.append(i)
    else:
        if dp[i+1] == dp[i] + A[i+1]:
            ans.append(i)
        else:
            i -= 1
            ans.append(i)
    i -= 1

print(len(ans))
print(*ans[::-1])