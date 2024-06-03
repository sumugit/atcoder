from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

N, X = map(int, input().split())
A = list(input())

queue = deque()
queue.append(X-1)
A[X-1] = '@'
while queue:
    pos = queue.popleft()
    if pos-1 >= 0 and A[pos-1] == '.':
        A[pos-1] = '@'
        queue.append(pos-1)
    if pos+1 < N and A[pos+1] == '.':
        A[pos+1] = '@'
        queue.append(pos+1)
print(*A, sep='')
