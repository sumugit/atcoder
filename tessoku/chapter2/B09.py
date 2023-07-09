N = int(input())
ABCD = [list(map(int, input().split())) for _ in range(N)]

# Create a 2D list filled with zeros
grid = [[0]*1501 for _ in range(1501)]
for a, b, c, d in ABCD:
    # 紙の一辺は 1-index
    grid[a+1][b+1] += 1
    if c+1 < 1501:
        grid[c+1][b+1] -= 1
    if d+1 < 1501:
        grid[a+1][d+1] -= 1
    if c+1 < 1501 and d+1 < 1501:
        grid[c+1][d+1] += 1

for i in range(1, 1501):
    for j in range(1, 1501):
        if i > 0:
            grid[i][j] += grid[i-1][j]
        if j > 0:
            grid[i][j] += grid[i][j-1]
        if i > 0 and j > 0:
            grid[i][j] -= grid[i-1][j-1]

ans = 0
for i in range(1, 1501):
    for j in range(1, 1501):
        if grid[i][j] > 0:
            ans += 1
print(ans)
