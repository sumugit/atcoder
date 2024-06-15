N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

ans = 0
b_idx = 0
for i in range(N):
    if A[i] >= B[b_idx]:
        ans += A[i]
        b_idx += 1
    if b_idx == M:
        break

if ans == 0 or b_idx < M:
    print(-1)
else:
    print(ans)