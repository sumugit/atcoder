from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

T = int(input())
n_list = [int(input()) for _ in range(T)]
candidates = range(60)
bit_search = []
for v in combinations(candidates, 3):
    bit_nums = ['0' for _ in range(60)]
    for i in v:
        bit_nums[i] = '1'
    bit_nums = ''.join(bit_nums)
    bit_search.append(int(bit_nums, 2))
bit_search = sorted(bit_search)

for N in n_list:
    # bit_seach から N 以下の最大値を探す
    max_idx = bisect_right(bit_search, N)
    # なければ -1
    if max_idx == 0:
        print(-1)
    else:
        print(bit_search[max_idx-1])
