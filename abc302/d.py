import bisect

N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
# B をソートする必要はない
ans = -1
for b in B:
    i = bisect.bisect_right(A, b + D) - 1
    if i >= 0 and b - A[i] <= D:
        ans = max(ans, A[i] + b)
print(ans)