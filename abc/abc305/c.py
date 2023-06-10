import numpy as np

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# 行ごとに#の数を数える
cks = []
nums = []
for i in range(H):
    cnt = 0
    for j in range(W):
        if S[i][j] == '#':
            cnt += 1
    if cnt > 0:
        cks.append(i)
        nums.append(cnt)

idx = np.argmin(nums)
pos_h = cks[idx]
if idx == len(cks)-1:
    next_h = cks[0]
else:
    next_h = pos_h+1

ans = [0, 0]
for j in range(W):
    if S[pos_h][j] != S[next_h][j]:
        ans = [pos_h+1, j+1]
        break
print(*ans)
