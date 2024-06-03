from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

S = input()
stack = deque()
for i in range(len(S)):
    if S[i] == '(':
        stack.append(i)
    elif S[i] == ')':
        if stack:
            left = stack.pop()
            right = i
            print(left+1, right+1)
