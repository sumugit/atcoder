N, D = map(int, input().split())
S = [input() for _ in range(N)]
f = [0] * D
for s in S:
    for i in range(D):
        if s[i] == 'o':
            f[i] += 1

start = -1
max_len = 0
for i in range(D):
    if f[i] == N:
        if start == -1:
            start = i
    elif f[i] != N and start != -1:
        max_len = max(max_len, i-start)
        start = -1

if start != -1:
    max_len = max(max_len, D-start)

print(max_len)