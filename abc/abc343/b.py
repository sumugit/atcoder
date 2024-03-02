from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    ans = []
    for j in range(N):
        if A[i][j] == 1:
            ans.append(j+1) 
    print(*ans)
