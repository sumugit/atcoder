from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = 0
for v in combinations(range(N), 2):
    n1, n2 = v
    flag = True
    for j in range(M):
        if S[n1][j] == 'x' and S[n2][j] == 'x':
            flag = False
            break
    if flag:
        ans += 1
print(ans)
