import numpy as np

N = int(input())
A = list(map(int, input().split()))

A_arg = np.argsort(A)
A_sort = np.sort(A)

cnt = 1
A_new = []
for i in range(N-1):
    A_new.append(cnt)
    if A_sort[i] < A_sort[i+1]:
        cnt += 1
A_new.append(cnt)

ans = [0] * N
for i in range(N):
    ans[A_arg[i]] = A_new[i]
    
print(*ans)