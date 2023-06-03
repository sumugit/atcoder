from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import numpy as np

N = int(input())
S = []
A = []
for i in range(N):
    s, a = input().split()
    S.append(s)
    A.append(int(a))

start = np.argmin(A)
ans_1 = S[start:]
ans_2 = S[:start]
for ans in ans_1:
    print(ans)
for ans in ans_2:
    print(ans)