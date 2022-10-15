N, Q = map(int, input().split())
L = []
a = []
for _ in range(N):
    ipt = list(map(int, input().split()))
    L.append(ipt[0])
    a.append(ipt[1:])
ans = []
for _ in range(Q):
    s, t = map(int, input().split())
    ans.append((s-1,t-1))

for i in range(Q):
    print(a[ans[i][0]][ans[i][1]])
