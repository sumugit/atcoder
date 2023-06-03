from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

W, H = map(int, input().split())
N = int(input())
pq = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

pd_dict = defaultdict(lambda: 0)
# 各p,qに対して二分探索
for p, q in pq:
    # p より大きい最小の値をaから二分探索
    p_id = bisect_right(a, p)
    # q に対してbを二分探索
    q_id = bisect_right(b, q)
    pd_dict[(p_id, q_id)] += 1

if len(pd_dict) < (A+1)*(B+1):
    m = 0
else:
    m = min(pd_dict.values())
M = max(pd_dict.values())
print(m, M)
