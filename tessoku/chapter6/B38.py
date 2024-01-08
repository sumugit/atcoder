N = int(input())
S = [-1] + list(input())

ans1 = [0] * N
ans2 = [0] * N

# 「<」のみ
cnt = 1
ans1[0] = cnt
for i in range(1, N):
    if S[i] == 'A':
        cnt += 1
    elif S[i] == 'B':
        cnt = 1
    ans1[i] = cnt

# 「>」のみ
cnt = 1
ans2[N-1] = cnt
for i in range(N-1, 0, -1):
    if S[i] == 'B':
        cnt += 1
    elif S[i] == 'A':
        cnt = 1
    ans2[i-1] = cnt

ans = [0] * N
for i in range(N):
    ans[i] = max(ans1[i], ans2[i])

print(sum(ans))
