from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

S = input()
dict_S = Counter(S)
dict_cnt = Counter(dict_S.values())
for val in dict_cnt.values():
    if val != 2:
        print('No')
        exit()

print('Yes')
