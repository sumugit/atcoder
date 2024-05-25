from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, T = map(int, input().split())
A = list(map(int, input().split()))

binary_bingo = [[False for _ in range(N)] for _ in range(N)]
dict_h_bingo = defaultdict(lambda: 0)
dict_v_bingo = defaultdict(lambda: 0)
dict_d1_bingo = 0
dict_d2_bingo = 0

for i in range(T):
    if not binary_bingo[(A[i]-1)//N][(A[i]-1)%N]:
        binary_bingo[(A[i]-1)//N][(A[i]-1)%N] = True
        dict_h_bingo[(A[i]-1)//N] += 1
        dict_v_bingo[(A[i]-1)%N] += 1
        if (A[i]-1)//N == (A[i]-1)%N:
            dict_d1_bingo += 1
        if (A[i]-1)//N + (A[i]-1)%N == N-1:
            dict_d2_bingo += 1
        if dict_h_bingo[(A[i]-1)//N] == N or dict_v_bingo[(A[i]-1)%N] == N or dict_d1_bingo == N or dict_d2_bingo == N:
            print(i+1)
            exit()
print(-1)
