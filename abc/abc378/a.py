from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

A = list(map(int, input().split()))
a_dict = defaultdict(lambda: 0)
for a in A:
    a_dict[a] += 1

ans = 0
for val in a_dict.values():
    ans += val//2
print(ans)