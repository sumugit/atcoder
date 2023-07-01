from collections import Counter, deque

def snuke(p_now, p_next):
    if p_now == 's' and p_next == 'n':
        return True
    elif p_now == 'n' and p_next == 'u':
        return True
    elif p_now == 'u' and p_next == 'k':
        return True
    elif p_now == 'k' and p_next == 'e':
        return True
    elif p_now == 'e' and p_next == 's':
        return True

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 幅優先探索
init_now = [[0, 0]]
init_p = S[0][0]
goal = [H-1, W-1]
queue = deque(init_now)
queue_p = deque(init_p)
while queue:
    now = queue.popleft()
    p_now = queue_p.popleft()
    S[now[0]][now[1]] = '◯'
    if now == goal:
        print("Yes")
        exit()
    for i in range(4):
        next = [now[0]+dir[i][0], now[1]+dir[i][1]]
        if 0 <= next[0] < H and 0 <= next[1] < W:
            p_next = S[next[0]][next[1]]
            if snuke(p_now, p_next):
                queue.append(next)
                queue_p.append(p_next)
                S[next[0]][next[1]] = '◯'
print("No")