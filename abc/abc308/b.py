from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

d_dict = defaultdict(lambda: 0)
for idx, d in enumerate(D):
    d_dict[d] = P[idx+1]

p_sum = 0
for c in C:
    if d_dict[c] > 0:
        p_sum += d_dict[c]
    else:
        p_sum += P[0]
print(p_sum)

