import numpy as np
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

H, W = map(int, input().split())
S = np.array([list(input()) for _ in range(H)])
T = np.array([list(input()) for _ in range(H)])

def enc_bi(lsts):
    binary = ''
    for val in lsts:
        if val == '#':
            binary += '0'
        elif val == '.':
            binary += '1'
    return int(binary, 2)

s = defaultdict(lambda: 0)
t = defaultdict(lambda: 0)
for w in range(W):
    s[enc_bi(S[:,w])] += 1
    t[enc_bi(T[:,w])] += 1
if s == t:
    print('Yes')
else:
    print('No')