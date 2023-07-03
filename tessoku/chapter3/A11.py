import bisect

N, X = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索
A = sorted(A)
idx = bisect.bisect_left(A, X)
if idx < N and A[idx] == X:
    print(idx+1)