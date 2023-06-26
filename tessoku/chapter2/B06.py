N = int(input())
A = list(map(int, input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for i in range(Q)]

loses = [0 for _ in range(N+1)] # N+1 にするのは, index を 1 スタートにするため
wins = [0 for _ in range(N+1)]
for i in range(1, N+1):
    loses[i] = loses[i-1]
    wins[i] = wins[i-1]
    if A[i-1] == 0:
        loses[i] += 1
    elif A[i-1] == 1:
        wins[i] += 1

for i in range(Q):
    L, R = LR[i]
    if wins[R] - wins[L-1] > loses[R] - loses[L-1]:
        print('win')
    elif wins[R] - wins[L-1] == loses[R] - loses[L-1]:
        print('draw')
    else:
        print('lose')
