from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

H, W, K = map(int, input().split())
S = [list(input().split()) for _ in range(H)]
S = [[char for char in inner_list[0]] for inner_list in S]
ans = 0

dir_list = [[-1, 0], [0, -1], [1, 0], [0, 1]]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        start = [i, j, K, [(i, j)]]
        stack = deque()
        stack.append(start)
        while len(stack) != 0:
            now_y, now_x, now_life, trace = stack.pop()
            if now_life == 0:
                ans += 1
                continue
            for dir in dir_list:
                new_y = now_y + dir[0]                
                new_x = now_x + dir[1]
                if now_life > 0 and 0 <= new_x <= W-1 and 0 <= new_y <= H-1 and S[new_y][new_x] != '#' and (new_y, new_x) not in trace:
                    new_life = now_life - 1
                    new_trace = trace + [(new_y, new_x)] #traceのコピーを作成する必要がある
                    stack.append([new_y, new_x, new_life, new_trace])    
print(ans)
