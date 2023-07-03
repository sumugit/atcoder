N, K = map(int, input().split())
A = list(map(int, input().split()))

sum_A = [0]
for i in range(N):
    sum_A.append(sum_A[i] + A[i])

left_idx = 0
right_idx = 1
ans = 0
while right_idx <= N:
    if sum_A[right_idx] - sum_A[left_idx] <= K:
        ans += 1
        right_idx += 1
        # 以下の 3 行忘れないように
        if right_idx > N:
            left_idx += 1
            right_idx = left_idx + 1
    else:
        left_idx += 1
        right_idx = left_idx + 1
print(ans)