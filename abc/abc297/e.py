N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

# 動的計画法で組み合わせ数を求める
dp = [0] * (sum(A) + 1)
dp[0] = 1
for i in range(N):
    for j in range(sum(A), A[i]-1, -1):
        dp[j] += dp[j-A[i]]

# K番目に小さいものを求める
count = 0
for i in range(sum(A) + 1):
    if dp[i] == 0:
        continue
    count += dp[i]
    if count >= K:
        print(i)
        break
