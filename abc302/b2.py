# define the grid
H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(H):
    for j in range(W):
        for k in range(8):
            s = ''
            for t in range(5):
                x = i + t*dx[k]
                y = j + t*dy[k]
                # 壁とのめり込み判定
                if x < 0 or x >= H or y < 0 or y >= W:
                    break
                s += S[x][y]
            if s == 'snuke':
                for t in range(5):
                    x = i + t*dx[k]
                    y = j + t*dy[k]
                    print(x+1, y+1)
                exit()
            