import numpy as np

H, W = map(int, input().split())
S_i, S_j = map(int, input().split())
C = [list(input()) for _ in range(H)]
X = list(input())

pos = np.array([S_i-1, S_j-1])
for i in range(len(X)):
    x, y = pos.copy()
    if X[i] == 'L' and y-1 >= 0 and C[x][y-1] == '.':
        pos[1] = y - 1
    elif X[i] == 'R' and y+1 <= W-1 and C[x][y+1] == '.':
        pos[1] = y + 1
    elif X[i] == 'U' and x-1 >= 0 and C[x-1][y] == '.':
        pos[0] = x - 1
    elif X[i] == 'D' and x+1 <= H-1 and C[x+1][y] == '.':
        pos[0] = x + 1
print(*[p+1 for p in pos])
