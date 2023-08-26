N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

# 隣接リスト
graph = [[] for _ in range(N)]
for a, b, c in ABC:
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

# a,bは街, c は長さ
# 好きな街からスタートして同じ街を二度以上通らずに別の街へ移動するときの、通る道路の長さの和としてありえる最大値
ans = 0
# 再帰関数で実装
def dfs(v, visited, cost, flag):
    global ans
    visited2 = visited.copy()
    visited2[v] = True
    for next_v, next_cost in graph[v]:
        if visited2[next_v]:
            continue
        dfs(next_v, visited2, cost + next_cost, flag)
    ans = max(ans, cost)

for i in range(N):
    if i == 3:
        dfs(i, [False]*N, 0, True)
    else:
        dfs(i, [False]*N, 0, False)
print(ans)