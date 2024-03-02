N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
ABC_sortC = sorted(ABC, key=lambda x: x[2])

class UnionFind:
    """ Union Find Tree """
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n  # 根は -1*(集合のノード数)

    def find(self, x):
        """ 根を参照するまで再帰 """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """ 木の連結 """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        # 頂点数が小さい親をy, 大きい親をxとなるようにマージする
        # この実装では頂点数*(-1) のため、値が小さい方が頂点数が大きい
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        # 小さいyの頂点数を大きいxの頂点数にマージ
        self.parents[x] += self.parents[y]
        # 小さいyの親を大きいxにする
        self.parents[y] = x

    def size(self, x):
        """ ノード数の取得 """
        return -self.parents[self.find(x)]

# クラスカル法による最小全域木のコスト計算
uf = UnionFind(N)
ans = 0
for a, b, c in ABC_sortC:
    if uf.find(a-1) != uf.find(b-1):
        ans += c
        uf.union(a-1, b-1)
print(ans)