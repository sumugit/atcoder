N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

if T in C:
    max_num = -1
    ans_idx = -1
    for idx in range(N):
        if T == C[idx]:
            if R[idx] > max_num:
                max_num = R[idx]
                ans_idx = idx+1
else:
    T = C[0]
    max_num = -1
    ans_idx = -1
    for idx in range(N):
        if T == C[idx]:
            if R[idx] > max_num:
                max_num = R[idx]
                ans_idx = idx+1
print(ans_idx)
    