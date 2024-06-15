from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

queue = deque()
N, A = map(int, input().split())
T = list(map(int, input().split()))

ans = [0] * N
for i in range(N):
    queue.append((i, T[i]))

sum_T = 0
while queue:
    i, t = queue.popleft()
    if sum_T <= t:
        ans[i] = t + A
        sum_T = t + A
    else:
        ans[i] = sum_T + A
        sum_T += A
for a in ans:
    print(a)