from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations
import math
MOD = 998244353

K = int(input())
C = list(map(int, input().split()))
sum_C = sum(C)
dict_C = Counter(C)

ans = 0
for i in range(1, K+1):
    tmp = math.perm(sum_C, i)
    for key, value in dict_C.items():
        if  key >= 2:
            tmp //= math.perm(key, i)*value
    ans += tmp%MOD
for num in range(1, K+1):
    for key, value in dict_C.items():
        if key >= 2:
            ans += dict_C[key]%MOD
print(ans%MOD)