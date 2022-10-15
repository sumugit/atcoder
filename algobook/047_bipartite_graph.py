import sys
# 再帰呼び出しの深さの上限を 210000 に設定 (これ設定しないと RE)
sys.setrecursionlimit(210000)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# 未探索 -1, 白 1, 黒 -1
color = [-1]*N
def dfs(graph, v, cur=0):
    color[v] = cur
    for next_v in graph[v]:
        if color[next_v] != -1:
            if color[next_v] == color[v]:
                return False
            continue
        if not dfs(graph, next_v, 1-cur):
            return False
    return True

is_bipartite = True
# 全ての頂点について調べる
for v in range(N):
    if color[v] != -1:
        continue
    if not dfs(graph, v):
        is_bipartite = False
if is_bipartite:
    print('Yes')
else:
    print('No')