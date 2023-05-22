from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
s_dict = defaultdict(lambda: 0)
sub1 = ['H', 'D', 'C', 'S']
sub2 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
flag1 = True
flag2 = True
flag3 = True
for i in range(N):
    s = input()
    if s[0] not in sub1:
        flag1 = False
    if s[1] not in sub2:
        flag2 = False
    s_dict[s] += 1
    if s_dict[s] > 1:
        flag3 = False
if flag1 and flag2 and flag3:
    print('Yes')
else:
    print('No')