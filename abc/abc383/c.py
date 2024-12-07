from collections import deque

H, W, D = map(int, input().split())
S = [input() for _ in range(H)] # 文字列のまま扱った方が高速化できる

floor_mass = [(i, j) for i in range(H) for j in range(W) if S[i][j] == 'H']

dir_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
trace = [[False] * W for _ in range(H)]

queue = deque()
for (hy, hx) in floor_mass:
    trace[hy][hx] = True
    queue.append((hy, hx, 0))

while queue:
    cur_y, cur_x, dist = queue.popleft()
    if dist == D:
        continue

    for dy, dx in dir_list:
        ny, nx = cur_y + dy, cur_x + dx
        if 0 <= ny < H and 0 <= nx < W:
            if not trace[ny][nx] and S[ny][nx] == '.':
                trace[ny][nx] = True
                queue.append((ny, nx, dist + 1))

ans = sum(sum(row) for row in trace)
print(ans)
