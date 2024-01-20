N = int(input())
A = list(map(int, input().split()))

adj = [[] for _ in range(N)]
now = -1
for idx, a in enumerate(A):
    if a == -1:
        now = idx
        continue
    adj[idx].append(a-1)
    adj[a-1].append(idx)

ans = [now+1]
cnt = 1
prev = -1
while cnt < N:
    for i in range(len(adj[now])):
        if adj[now][i] != prev:
            ans.append(adj[now][i]+1)
            prev = now
            now = adj[now][i]
            cnt += 1
            break
print(*ans)

