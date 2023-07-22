# While True が原因で TLE になっていた 
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False]*M for _ in range(N)]
stopped = [[False]*M for _ in range(N)]
start = (2-1, 2-1)  # (2, 2) to 0-indexed
queue = deque([start])

def dfs(x, y):
    ice_count = 0
    visited[x][y] = True
    stopped[x][y] = True
    ice_count += 1
    while queue:
        now = queue.popleft()
        x, y = now
        for i in range(4):
            nx, ny = x, y
            while S[nx+dx[i]][ny+dy[i]] == ".":
                nx, ny = nx+dx[i], ny+dy[i]
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    ice_count += 1
            if not stopped[nx][ny]:
                stopped[nx][ny] = True
                queue.append((nx, ny))
    
    return ice_count

ice_cnt = dfs(*start)
print(ice_cnt)