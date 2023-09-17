# from collections import Counter, deque, defaultdict
# import numpy as np

# N, M = map(int, input().split())
# ABXY = [list(map(int, input().split())) for _ in range(M)]
# ABXY2 = []
# points = defaultdict(lambda: [np.nan, np.nan])
# points[1] = [0, 0]

# for i in range(M):
#     a, b, x, y = ABXY[i]
#     if a > b:
#         x2, y2 = -x, -y
#         ABXY2.append([b, a, x2, y2])
#     else:
#         ABXY2.append([a, b, x, y])

# ABXY2 = sorted(ABXY2, key=lambda x: x[0])

# for i in range(M):
#     a, b, x, y = ABXY2[i]        
#     if a == 1:
#         new_x, new_y = x, y
#         if not np.isnan(points[b][0]) and not np.isnan(points[b][1]):
#             if points[b][0] != new_x or points[b][1] != new_y:
#                 points[b] = [np.nan, np.nan]
#         else:
#             points[b] = [new_x, new_y]
#     else:
#         new_x, new_y = [points[a][0]+x, points[a][1]+y]
#         if not np.isnan(points[b][0]) and not np.isnan(points[b][1]):
#             if points[b][0] != new_x or points[b][1] != new_y:
#                 points[b] = [np.nan, np.nan]
#         else:
#             points[b] = [new_x, new_y]

# for i in range(N):
#     if np.isnan(points[i+1][0]):
#         print("undecidable")
#     else:
#         print(points[i+1][0], points[i+1][1])

# 再帰DFS (グラフのDFSは再帰で書くのが一般的)
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, x, y))
    G[b].append((a, -x, -y))

pos = [(None, None) for _ in range(n)]
visited = [False for _ in range(n)]

def dfs(v, x, y):
    visited[v] = True
    pos[v] = (x, y)
    for vv, dx, dy in G[v]:
        if not visited[vv]:
            dfs(vv, x + dx, y + dy)

dfs(0, 0, 0)
for i in range(n):
    if visited[i]:
        print(pos[i][0], pos[i][1])
    else:
        print("undecidable")
