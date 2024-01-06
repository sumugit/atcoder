class UnionFind:
    def __init__(self, size):
        self.data = [-1] * size

    def union_set(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.data[y] < self.data[x]:
                x, y = y, x
            self.data[x] += self.data[y]
            self.data[y] = x
        return x != y

    def find_set(self, x, y):
        return self.root(x) == self.root(y)

    def root(self, x):
        if self.data[x] < 0:
            return x
        self.data[x] = self.root(self.data[x])
        return self.data[x]

    def size(self, x):
        return -self.data[self.root(x)]


n, m = map(int, input().split())
a = list(map(int, input().split()))

uf = UnionFind(n)
vp = [[] for _ in range(200005)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if a[u] > a[v]: # 一般性を失わない
        # こうすると DAG として問題を解ける
        # DAG なので DP ができる
        # (トポロジカルソートして DP する)
        u, v = v, u
    if a[u] == a[v]:
        uf.union_set(u, v)
    else:
        vp[a[u]].append((u, v))

dp = [-1e9] * 200005
dp[uf.root(0)] = 1

for nx in vp:
    for u, v in nx:
        u = uf.root(u) # 値が同じ頂点対を結合した後のユニークな頂点
        v = uf.root(v)
        if dp[u] > 0:
            dp[v] = max(dp[v], dp[u] + 1)

print(max(0, dp[uf.root(n - 1)]))
