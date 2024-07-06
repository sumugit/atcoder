import math
N, K = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
ans = math.inf
for i in range(K+1):
    # スライディングウィンドウ
    ans = min(ans, A[i+N-K-1] - A[i])
print(ans)
