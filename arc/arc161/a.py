from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))

A_sorted = sorted(A, reverse=True)
even_group = deque(A_sorted[:N//2])
odd_group = deque(A_sorted[N//2:])
m_A = []
while len(even_group) > 0 or len(odd_group) > 0:
    if len(odd_group) > 0:
        m_A.append(odd_group.popleft())
    if len(even_group) > 0:
        m_A.append(even_group.popleft())

for i in range(1, N-1, 2):
    if not (m_A[i-1] < m_A[i] > m_A[i+1]):
        print('No')
        exit()
print('Yes')
