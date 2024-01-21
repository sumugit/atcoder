import random
import time

N = 100
A = [list(map(int, input().split())) for _ in range(N)]
B = [[0] * N for _ in range(N)]

XYH = []
Q = 1000
for q in range(Q):
    x = random.randint(0, N-1)
    y = random.randint(0, N-1)
    h = 1
    B[y][x] = h
    XYH.append([y, x, h])

def get_score():
    sum = 0
    for i in range(N):
        for j in range(N):
            sum += abs(A[i][j] - B[i][j])
    return 200000000 - sum # 87595820

def change(t, x, y, h):
    # 計算量の工夫 (B の更新箇所のみ事前に計算する)
    pre_x, pre_y, pre_h = XYH[t]
    for i in range(N):
        for j in range(N):
            B[i][j] -= max(0, pre_h - abs(pre_x-i) - abs(pre_y-j))
    
    # 局所探索
    XYH[t][0] = y
    XYH[t][1] = x
    XYH[t][2] = h
    
    # B の更新    
    for q in range(Q):
        x, y, h = XYH[q]
        for i in range(N):
            for j in range(N):
                B[i][j] += max(0, h - abs(x-i) - abs(y-j))

def yamanobori():
    TIMELIMIT = 5.4
    current_score = get_score()
    ti = time.time()
    
    while time.time() - ti < TIMELIMIT:
        t = random.randint(0, Q-1)
        old_x, old_y, old_h = XYH[t]
        new_x = old_x + random.randint(-9, 9)
        new_y = old_y + random.randint(-9, 9)
        new_h = old_h + random.randint(-19, 19)
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or new_h <= 0:
            continue
        change(t, new_x, new_y, new_h)
        new_score = get_score()
        if new_score > current_score:
            current_score = new_score
        else:
            change(t, old_x, old_y, old_h)

# print(get_score())
yamanobori()
#print(get_score())
print(Q)
for i in range(Q):
    print(*XYH[i])