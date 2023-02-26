from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
S = input()

stk_lr = 0
stk_ud = 0
trace = defaultdict(lambda: False)
trace[(stk_lr, stk_ud)] = True

for idx, s in enumerate(S):
    if s == 'R':
        stk_lr += 1
    elif s == 'L':
        stk_lr -= 1
    elif s == 'U':
        stk_ud += 1
    elif s == 'D':
        stk_ud -= 1
    if trace[(stk_lr, stk_ud)]:
        print('Yes')
        exit()
    else:
        trace[(stk_lr, stk_ud)] = True
print('No')