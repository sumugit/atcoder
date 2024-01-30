from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

# 距離が最小の頂点から確定させていけば、絶対に最短経路が求まる
N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

graph = defaultdict(lambda: [])
for i in range(M):
    graph[ABC[i][0]].append((ABC[i][1], ABC[i][2]))
    graph[ABC[i][1]].append((ABC[i][0], ABC[i][2]))

kakutei = [False] * (N+1)
cur = [2000000000] * (N+1)
cur[1] = 0
q = []
heappush(q, (cur[1], 1))

# ダイクストラ法
while len(q) > 0:
    # 未確定頂点の中でcurの値が最も小さい頂点posを求める
    # 優先度付きキューを使うと、O(logN)で最小値を取り出せる
    dist, pos = heappop(q)
    if kakutei[pos]:
        continue
    kakutei[pos] = True
    
    # 頂点pos に隣接する頂点について、curの値を更新する (DP)
    for i in range(len(graph[pos])):
        next_v = graph[pos][i][0]
        next_dis = graph[pos][i][1]
        if cur[next_v] > cur[pos] + next_dis:
            cur[next_v] = cur[pos] + next_dis
            heappush(q, (cur[next_v], next_v))

for i in range(1, N+1):
    if cur[i] == 2000000000:
        print(-1)
    else:
        print(cur[i])