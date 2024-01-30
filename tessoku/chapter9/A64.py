from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

graph = defaultdict(lambda: [])
for i in range(M):
    graph[ABC[i][0]].append((ABC[i][1], ABC[i][2]))
    graph[ABC[i][1]].append((ABC[i][0], ABC[i][2]))

kakutei = [False] * (N+1)
cur = [2000000000] * (N+1)
cur[1] = 0
while True:
    # 未確定頂点の中でcurの値が最も小さい頂点posを求める
    pos = -1
    mindist = 2000000000
    # 最も小さい値を持つ頂点を探すのに、O(N)かかってしまう
    for i in range(1, N+1):
        if not kakutei[i] and cur[i] < mindist:
            mindist = cur[i]
            pos = i
    if pos == -1:
        break
    kakutei[pos] = True
    
    # 頂点pos に隣接する頂点について、curの値を更新する (DP)
    for i in range(len(graph[pos])):
        next_v = graph[pos][i][0]
        next_dis = graph[pos][i][1]
        cur[next_v] = min(cur[next_v], cur[pos] + next_dis)

for i in range(1, N+1):
    if cur[i] == 2000000000:
        print(-1)
    else:
        print(cur[i])