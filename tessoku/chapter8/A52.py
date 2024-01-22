from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

Q = int(input())
query = [list(input().split()) for _ in range(Q)]

queue = deque()

for q in query:
    if len(q) == 1:
        num = q[0]
    else:
        num, x = q
    if num == "1":
        queue.append(x)
    elif num == "2":
        print(queue[0])
    else:
        queue.popleft()