from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = [int(input()) for _ in range(Q)]

A = sorted(A)
for i in range(Q):
    idx = bisect_left(A, X[i])
    print(idx)