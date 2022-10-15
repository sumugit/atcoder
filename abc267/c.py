N, M = map(int, input().split())
A = list(map(int, input().split()))

def exp_val(A):
    ans = 0
    for idx, val in enumerate(A):
        ans += (idx+1)*val
    return ans

max_sum = exp_val(A[:M])
ans_pre_sum = max_sum
pre_sum = sum(A[:M])
for i in range(1, N-M+1):
    next_sum = ans_pre_sum - pre_sum + M*A[i+M-1]
    max_sum = max(next_sum, max_sum)
    pre_sum = pre_sum -A[i-1] + A[i+M-1]
    ans_pre_sum = next_sum

print(max_sum)