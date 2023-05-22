import numpy as np

N = int(input())
A = list(map(int, input().split()))

P = 0
spot = np.zeros(N)
ans = np.zeros(N)

for i in range(N):
    for j in range(i+1):
        spot[j] += A[i]
        if spot[j] >= 4:
            ans[j] = 1

print(int(sum(ans)))