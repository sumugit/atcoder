import numpy as np
R, C = map(int, input().split())

A = np.zeros(shape=(15, 15), dtype=int)
B = np.zeros(shape=(15, 15), dtype=int)
cnt = 0
for i in range(15):
    if i%2 == 1:
        cnt += 1
        for j in range(i, i + 17-4*cnt):
            A[i, j] = 1
A = A + A.T
cnt = 0
for i in reversed(range(15)):
    if i%2 == 1:
        cnt += 1
        for j in range(15-i-1, 15-i-1 + 17-4*cnt):
            B[i, j] = 1

B = B + B.T
A = A + B

if A[R-1, C-1] > 0:
    print('white')
else:
    print('black')
