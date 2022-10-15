N, M = map(int, input().split())
graph = [0 for _ in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    if a-1 > b-1:
        graph[a-1] += 1
    elif b-1 > a-1:
        graph[b-1] += 1 
    # graph[a-1].append(b-1)
    # graph[b-1].append(a-1)

ans = 0
for node in graph:
    if node == 1:
        ans += 1
print(ans)

