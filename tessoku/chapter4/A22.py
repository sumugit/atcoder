N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

# 配るDP
dp = [-1] * (100009)
dp[1] = 0

for i in range(1, N):
    # 絶対通らないマスは更新しない
    if dp[i] == -1:
        continue
    else:
        dp[A[i]] = max(dp[A[i]], dp[i] + 100)
        dp[B[i]] = max(dp[B[i]], dp[i] + 150)

print(max(dp))