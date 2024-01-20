H, W, K = map(int, input().split())
S = ['#'] + [['#'] + list(input()) for _ in range(H)]

def find_min_pattern(H, W, K, grid):
    # Initialize variables
    X = [0] * (W + 1)
    D = [0] * (W + 1)
    ans = float('inf')

    # Processing rows
    for y in range(1, H + 1):
        for i in range(1, W + 1):
            # この2行で X, D は上書きされるため, X, D は1次元配列で十分
            X[i] = X[i-1]
            D[i] = D[i-1]
            if grid[y][i] == 'x':
                X[i] += 1
            if grid[y][i] == '.':
                D[i] += 1
        for i in range(1, W - K + 2):
            if X[i+K-1] - X[i-1] == 0:
                ans = min(ans, D[i+K-1] - D[i-1])

    # Re-initialize variables for columns
    X = [0] * (H + 1)
    D = [0] * (H + 1)

    # Processing columns
    for x in range(1, W + 1):
        for i in range(1, H + 1):
            X[i] = X[i-1]
            D[i] = D[i-1]
            if grid[i][x] == 'x':
                X[i] += 1
            if grid[i][x] == '.':
                D[i] += 1
        for i in range(1, H - K + 2):
            if X[i+K-1] - X[i-1] == 0:
                ans = min(ans, D[i+K-1] - D[i-1])
    if ans > K:
        ans = -1
    return ans

ans = find_min_pattern(H, W, K, S)
print(ans)
