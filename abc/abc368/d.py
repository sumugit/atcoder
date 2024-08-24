N,K = map(int,input().split())
edge = [set() for _ in range(N)]

for _ in range(N-1):
  a,b = map(int,input().split())
  a-=1
  b-=1
  edge[a].add(b)
  edge[b].add(a)

V = set(map(int,input().split()))
V = set(x-1 for x in V)

deg = [len(s) for s in edge]
q = [i for i,d in enumerate(deg) if d==1]

ans = N
for v in q:
  if v in V: continue
  vv = edge[v].pop()
  edge[vv].discard(v)
  ans-=1
  if len(edge[vv])==1: q.append(vv)

print(ans)

