from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c_xy = [input() for _ in range(R)]

arr_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
arr_ans = [[-1]*C for _ in range(R)]
now = (sy-1, sx-1)
goal = (gy-1, gx-1)

d = deque()
d.append(now)
arr_ans[now[0]][now[1]] = 0
while len(d) != 0:
    now = d.popleft()
    for dir in arr_dir:
        next_x = now[0] + dir[0]
        next_y = now[1] + dir[1]
        if 0 <= next_x <= R-1 and 0 <= next_y <= C-1:
            if c_xy[next_x][next_y] != '#' and arr_ans[next_x][next_y] < 0:
                d.append((next_x, next_y))
                arr_ans[next_x][next_y] = arr_ans[now[0]][now[1]] + 1

# print(arr_ans)
print(arr_ans[goal[0]][goal[1]])

