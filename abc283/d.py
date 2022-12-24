from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
S = input()
ball_dict = defaultdict(lambda: False)
stack1 = deque()
stack2 = deque()
for idx, s in enumerate(S):
    if s == '(':
        stack1.appendleft(idx)
    elif s == ')':
        max_j = stack1.popleft()
        while True:
            if len(stack2) == 0:
                break
            alf, num = stack2.popleft()
            if num < max_j:
                stack2.appendleft((alf, num))
                break
            else:
                ball_dict[alf] = False
    else:
        if ball_dict[s]:
            print('No')
            exit()
        else:
            stack2.appendleft((s, idx))
            ball_dict[s] = True
print('Yes')