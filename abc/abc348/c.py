from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
AC = [list(map(int, input().split())) for _ in range(N)]

col_min_dict = defaultdict(lambda: 10**9)
for a, c in AC:
    col_min_dict[c] = min(col_min_dict[c], a)

ans = max(col_min_dict.values())
print(ans)