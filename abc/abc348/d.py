from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
N = int(input())
RCE = [list(map(int, input().split())) for _ in range(N)]

start, goal = None, None
for i in range(H):
    for j in range(W):
        if S[i][j] == "S":
            start = [i, j]
        elif S[i][j] == "T":
            goal = [i, j]

for r, c, e in RCE:
    r, c = r-1, c-1
    if [r, c] == start:
        start.append(e)
    S[r][c] = str(e) if S[r][c] not in ["S", "T"] else S[r][c]

if len(start) != 3:
    print("No")
else:
    def bfs():
        visited = [[-1] * W for _ in range(H)]
        visited[start[0]][start[1]] = start[2]
        queue = deque([start])
        while queue:
            y, x, life = queue.popleft()
            if [y, x] == goal:
                return True
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W and S[ny][nx] != "#" and life > 0:
                    new_life = life - 1
                    if S[ny][nx].isdigit():
                        energy = int(S[ny][nx])
                        new_life = max(energy, new_life)
                    if new_life > visited[ny][nx]:
                        visited[ny][nx] = new_life
                        queue.append((ny, nx, new_life))
        return False

    print("Yes" if bfs() else "No")
