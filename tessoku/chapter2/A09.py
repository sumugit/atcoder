H, W, N = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(N)]

# 二次元のimos法
imos_HW = [[0] * (W+1) for _ in range(H+1)]
for i in range(N):
    a, b, c, d = ABCD[i]
    imos_HW[a][b] += 1
    if d+1 < W+1:
        imos_HW[a][d+1] -= 1
    if c+1 < H+1:
        imos_HW[c+1][b] -= 1
    if c+1 < H+1 and d+1 < W+1:
        imos_HW[c+1][d+1] += 1

# 横方向の累積和
for i in range(1, H+1):
    for j in range(1, W+1):
        imos_HW[i][j] += imos_HW[i][j-1]

# 縦方向の累積和
for i in range(1, H+1):
    for j in range(1, W+1):
        imos_HW[i][j] += imos_HW[i-1][j]

for i in range(1, H+1):
    print(*imos_HW[i][1:W+1])