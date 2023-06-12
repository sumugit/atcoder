from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))
triangle_num = [0 for _ in range(100+1)]
for a in A:
    triangle_num[a] += 1
ans = 0
for i in range(len(triangle_num)):
    if triangle_num[i] > 2:
        ans += triangle_num[i]*(triangle_num[i]-1)*(triangle_num[i]-2)//6
print(ans)