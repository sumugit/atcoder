N = int(input())
A = list(map(int, input().split()))
D = int(input())
LR = [list(map(int, input().split())) for _ in range(D)]

max_acmod_left = [A[0]]
for i in range(1, N):
    max_acmod_left.append(max(max_acmod_left[i-1], A[i]))

B = A[::-1]
max_acmod_right = [B[0]]
for i in range(1, N):
    max_acmod_right.append(max(max_acmod_right[i-1], B[i]))


for i in range(D):
    l, r = LR[i]
    print(max(max_acmod_left[l-2], max_acmod_right[N-r-1]))