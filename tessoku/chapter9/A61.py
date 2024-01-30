from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

graph = defaultdict(lambda: set())
for i in range(M):
    graph[AB[i][0]].add(AB[i][1])
    graph[AB[i][1]].add(AB[i][0])

for i in range(1, N+1):
    if len(graph[i]) == 0:
        print(f'{i}: ' + '{}')
    else:
        print(f'{i}: ' + str(graph[i]))