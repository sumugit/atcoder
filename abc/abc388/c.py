from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    num = bisect_right(A, 2*a)
    if num > 0 and A[num-1] == 2*a:
        num = bisect_left(A, 2*a)
    ans += N - num
print(ans)
