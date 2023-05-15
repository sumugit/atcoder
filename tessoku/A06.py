N, Q = map(int, input().split())
A = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(Q)]

sum_A = [0]
for i in range(N):
    sum_A.append(sum_A[i] + A[i])
for i in range(Q):
    l, r = LR[i]
    # 「r 日目から」より, 左は l-1 日目から
    print(sum_A[r] - sum_A[l-1])
