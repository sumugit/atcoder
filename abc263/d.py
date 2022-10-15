import numpy as np
N, L, R = map(int, input().split())
A = list(map(int, input().split()))

"""
配列の要素更新は計算量が膨大 (全探索)
"""
"""
avg = []
for i in range(N):
    avg.append(np.mean(A[:i]))
if max(avg) <= L:
    x = 0
else:
    x = np.argmax(avg)
    for k in range(x + 1):
        A[k] = L

avg = []
for i in range(N):
    j = N - i - 1
    avg.append(np.mean(A[j:]))
if max(avg) <= R:
    y = 0
else:
    y = np.argmax(avg)
    for k in range(y + 1):
        A[N - k + 1] = R

print(np.sum(A))
"""

ans_l = np.zeros(N, dtype=int)
ans_l[0] = min(L, A[0])
# 左から
for i in range(1, N):
    ans_l[i] = min(ans_l[i-1] + A[i], L*(i+1))

ans = N * R
# 右から
for i in reversed(range(1, N+1)):
    ans = min(ans, (N - i)*R + ans_l[i-1])

print(ans)

