from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

graph = defaultdict(lambda: [])
for i in range(M):
    graph[AB[i][0]].append(AB[i][1])
    graph[AB[i][1]].append(AB[i][0])

queue = deque()
queue.append((1, 0))
visited = [False] * (N+1)
visited[1] = True
min_dis = [-1] * (N+1)
min_dis[1] = 0
while len(queue) > 0:
    v, dis = queue.popleft()
    for next_v in graph[v]:
        if not visited[next_v]:
            visited[next_v] = True
            min_dis[next_v] = dis + 1
            queue.append((next_v, dis+1))

for i in range(1, N+1):
    print(min_dis[i])