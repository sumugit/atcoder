from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

N, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

G = [list() for _ in range(2005)]
for i in range(N):
    x, y = XY[i]
    G[x].append(y)

ans = 0
Q = []
for i in range(1, D+1):
    for y in G[i]:
        heappush(Q, -y)
    if Q:
        ans += -heappop(Q)
print(ans)