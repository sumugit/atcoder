N, K = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)

def check(t):
    sum = 0
    for i in range(N):
        sum += t//A[i]
    if sum >= K:
        return True
    return False

# 二分探索
left = 1
right = 10**9
while right - left >= 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    if not check(mid):
        left = mid + 1
# left == right になる
print(right)
