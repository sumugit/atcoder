N, M = map(int, input().split())
P = list(map(int, input().split()))
mod = 998244353

# 辞書順の対称性とグラフの連結成分を考える
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
        # 大きい集合に小さい集合を merge
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """ ノード数の取得 """
        return -self.parents[self.find(x)]

def modpow(a: int, b: int, m: int, lim: int) -> int:
    """ 
    繰り返し二乗法 O(logb)
    a^b を mod で割った余りを出力
    lim : mod で割る数を2進数にした時の桁数 (10^3 ~ 2^10)
    """
    p = a
    ans = 1
    for i in range(lim):
        if b & (1 << i) != 0:
            ans *= p
            ans %= m
        p *= p
        p %= m
    return ans

def division(a: int, b: int, m, lim: int) -> int:
    """
    a÷b mod m を返す関数
    フェルマーの小定理を使う
    """
    return (a*modpow(b, m-2, m, lim))%m

tree = UnionFind(N)
for i in range(N):
    tree.union(i, P[i]-1)
# 連結成分の個数取得
result = 0
for i in range(N):
    if tree.find(i) == i:
        result += 1
ans = division(modpow(M,N,mod,30)-modpow(M,result,mod,30),2,mod,30)
print(ans%mod)