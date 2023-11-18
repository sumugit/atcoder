from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = map(int, input().split())
S = input()
S_list = list(S)
T = input()


queue = deque()
for i in range(N-M+1):
    if S[i:M+i] == T:
        queue.append(i)

while queue:
    i = queue.popleft()
    S_list[i:i+M] = ['#']*M
    for j in range(i-M, i+M+1):
        if j < 0 or j > N-M:
            continue
        flag = True
        flag2 = False
        for k in range(j, j+M):
            if S_list[k] != '#' and S[k] != T[k-j]:
                flag = False
                break
            # '#'に切り替わっていない数字がまだあるか (無限ループ防止)
            if S_list[k] == S[k]:
                flag2 = True
        if flag and flag2:
            queue.append(j)

ans = S_list.count('#')
if ans == N:
    print('Yes')
else:
    print('No')