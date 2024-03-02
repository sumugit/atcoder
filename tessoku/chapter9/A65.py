from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [0, 0] + list(map(int, input().split()))
tree = defaultdict(lambda: [])

for i in range(2, N+1):
    tree[A[i]].append(i)

dp = [0] * (N+1)
for i in range(N, 0, -1):
    if len(tree[i]) == 0:
        dp[i] = 0
    else:
        dp[i] = sum([dp[j]+1 for j in tree[i]])

print(*dp[1:N+1])