N = int(input())
A = list(map(int, input().split()))
MOD = 10**8

ans = 0
# 各項は N-1 回足される法則がある
sum_pair = (N-1)*sum(A)
sorted_A = sorted(A)
# 尺取り法で < 10**18 となる組み合わせを数える
num = 0
i = 0
r = N
for i in range(N):
    r = max(i+1, r)
    while r-1 > i and sorted_A[r-1] + sorted_A[i] >= MOD:
        r -= 1
    num += N - r
ans = sum_pair - MOD*num
print(ans)
