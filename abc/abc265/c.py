H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]
cnf = [[0]*W for _ in range(H)]

now = [0, 0]
while True:
    pre_now = now.copy()
    if G[now[0]][now[1]] == 'U' and now[0] != 0:
        now = [now[0]-1, now[1]]
    elif G[now[0]][now[1]] == 'D' and now[0] != H-1:
        now = [now[0]+1, now[1]]
    elif G[now[0]][now[1]] == 'L' and now[1] != 0:
        now = [now[0], now[1]-1]
    elif G[now[0]][now[1]] == 'R' and now[1] != W-1:
        now = [now[0], now[1]+1]
    if pre_now == now:
        print(now[0]+1, now[1]+1)
        break
    if cnf[now[0]][now[1]] == 1:
        print(-1)
        break
    cnf[now[0]][now[1]] = 1