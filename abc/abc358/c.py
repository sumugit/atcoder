from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
for i in range(N):
    S[i] = [1 if s == 'o' else 0 for s in S[i]]

ans = 11
for n in range(1, N+1):
    for comb in combinations(range(N), n):
        tmp = [0] * M
        for m in comb:
            tmp = [tmp[i] | S[m][i] for i in range(M)]
        if sum(tmp) == M:
            ans = min(ans, n)
print(ans)