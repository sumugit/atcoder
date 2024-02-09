from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))
ans_lst = []

stack = deque()
for i in range(N):
    if not stack:
        stack.append([A[i], i])
        ans_lst.append(-1)
    else:
        a, idx = stack[-1]
        if a < A[i]:
            while stack and stack[-1][0] < A[i]:
                stack.pop()
        if stack:
            ans, ans_idx = stack[-1]
            ans_lst.append(ans_idx+1)
            stack.append([A[i], i])
        else:
            stack.append([A[i], i])
            ans_lst.append(-1)
print(*ans_lst)