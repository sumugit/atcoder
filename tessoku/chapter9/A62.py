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

stack = deque()
stack.append(1)
visited = [False] * (N+1)
visited[1] = True
while len(stack) > 0:
    v = stack.pop()
    for next_v in graph[v]:
        if not visited[next_v]:
            visited[next_v] = True
            stack.append(next_v)

if all(visited[1:]):
    print('The graph is connected.')
else:
    print('The graph is not connected.')

# 再帰関数でも実装できる