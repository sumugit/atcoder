from collections import defaultdict, deque

N, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

def is_neighbor(x1, y1, x2, y2, D):
    return (x1-x2)**2 + (y1-y2)**2 <= D**2

neighbors = defaultdict(list)
for i in range(N):
    for j in range(i+1, N):
        if is_neighbor(XY[i][0], XY[i][1], XY[j][0], XY[j][1], D):
            neighbors[i].append(j)
            neighbors[j].append(i)

virus_dict = defaultdict(lambda: False)
virus_dict[0] = True
queue = deque([0])
while queue:
    now = queue.popleft()
    for next_node in neighbors[now]:
        if not virus_dict[next_node]:
            queue.append(next_node)
            virus_dict[next_node] = True

for i in range(N):
    if virus_dict[i]:
        print("Yes")
    else:
        print("No")
