from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M, H, K = map(int, input().split())
S = input()
xy = [list(map(int, input().split())) for _ in range(M)]
dxdy_dict = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}
life_dict = defaultdict(lambda: False)
for x, y in xy:
    life_dict[(x, y)] = True

life = H
now = [0, 0]
for s in S:
    dx, dy = dxdy_dict[s]
    now[0] += dx
    now[1] += dy
    life -= 1
    if life < 0:
        print('No')
        exit()
    if life_dict[tuple(now)] and life < K:
        life = K
        life_dict[tuple(now)] = False
print('Yes')
