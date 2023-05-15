from collections import deque, defaultdict

N, M = map(int, input().split())
graph = defaultdict(lambda: [])
nodes = [-1] * (N+1)
traces = [False] * (N+1)
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
d = deque([])
cur_node = 1
d.append(cur_node)
traces[cur_node] = True
nodes[cur_node] = 0
while len(d) > 0:
    cur_node = d.popleft()
    for node in graph[cur_node]:
        if not traces[node]:
            d.append(node)    
            traces[node] = True
            nodes[node] = min(nodes[cur_node] + 1, 120)
for i in range(1, N+1):
    if nodes[i] == -1:
        print(120)
    else:
        print(nodes[i])
