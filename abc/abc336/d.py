N = int(input())
A = list(map(int, input().split()))

left = [0] * N
right = [0] * N
# left to right
for i in range(N):
    if i == 0:
        left[i] = 1
    else:
        left[i] = min(left[i-1] + 1, A[i])
# right to left
for i in range(N-1, -1, -1):
    if i == N-1:
        right[i] = 1
    else:
        right[i] = min(right[i+1] + 1, A[i])

ans = 0
for i in range(N):
    ans = max(ans, min(left[i], right[i]))
print(ans)
