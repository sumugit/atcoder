from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))
B = []

b_dict = defaultdict(lambda: -1)
for i in range(len(A)):
    B.append(b_dict[A[i]])    
    if b_dict[A[i]] <= i:
        b_dict[A[i]] = i+1
print(*B)