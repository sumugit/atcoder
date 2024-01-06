N = int(input())

grid = [[0] * N for _ in range(N)]
grid[(N-1)//2][(N-1)//2] = 'T'

def fill_spiral(N):
    # N×N のグリッドを初期化
    grid = [[0]*N for _ in range(N)]

    num = 1
    for layer in range((N+1)//2):
        # 上辺を埋める
        for i in range(layer, N-layer):
            grid[layer][i] = num
            num += 1

        # 右辺を埋める
        for i in range(layer + 1, N - layer):
            grid[i][N-layer-1] = num
            num += 1

        # 下辺を埋める
        for i in range(N-layer-2, layer-1, -1):
            grid[N-layer-1][i] = num
            num += 1

        # 左辺を埋める
        for i in range(N-layer-2, layer, -1):
            grid[i][layer] = num
            num += 1

    return grid

grid = fill_spiral(N)
grid[(N-1)//2][(N-1)//2] = 'T'
for row in grid:
    print(*row)