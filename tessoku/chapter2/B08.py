import numpy as np

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
abcd = [list(map(int, input().split())) for _ in range(Q)]

grid = np.zeros((1500, 1500), dtype=np.int64)
for x, y in XY:
    grid[x-1, y-1] += 1
for i in range(1500):
    for j in range(1500):
        if i > 0:
            grid[i, j] += grid[i-1, j]
        if j > 0:
            grid[i, j] += grid[i, j-1]
        # 重複分を引く (斜め上のマスは, 左と上で既に足されているので, 現在地では重複している)
        if i > 0 and j > 0:
            grid[i, j] -= grid[i-1, j-1]
for a, b, c, d in abcd:
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    ans = grid[c, d]
    if a > 0:
        ans -= grid[a-1, d]
    if b > 0:
        ans -= grid[c, b-1]
    if a > 0 and b > 0:
        ans += grid[a-1, b-1]
    print(int(ans))