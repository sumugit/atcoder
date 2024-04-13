N = int(input())
A = list(map(int, input().split()))

A_ans = [0] * N
for i in range(N-1):
    tmp = A_ans[i]
    if A[i] > A_ans[i]:
        A_ans[i] += A[i] - tmp
        A_ans[i+1] -= A[i] - tmp
    elif A[i] < A_ans[i]:
        A_ans[i] -= tmp - A[i]
        A_ans[i+1] += tmp - A[i]

print(A_ans[N-1])