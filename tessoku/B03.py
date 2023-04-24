from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))
# A の中から3つを選び全探索
for r in combinations(A, 3):
    # 3つの和が3の倍数か判定
    if sum(r) == 1000:
        print('Yes')
        exit()
print('No')