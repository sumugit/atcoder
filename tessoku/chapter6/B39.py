N, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
XY = sorted(XY, key=lambda x: x[0])

task_list = []
ans = 0
pos = 0
for i in range(1, D+1):
    if pos < N:
        x, y = XY[pos]
        while i == x:
            task_list.append(y)
            pos += 1
            if pos >= N:
                break
            x, y = XY[pos]
    if len(task_list) > 0:
        max_y = max(task_list)
        ans += max_y
        task_list.remove(max_y)

print(ans)