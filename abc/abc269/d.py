import collections

# Union Find
class UnionFind:
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


def check(pos1, pos2):
    if pos1[0]-1 == pos2[0] and pos1[1]-1 == pos2[1]:
        return True
    elif pos1[0]-1 == pos2[0] and pos1[1] == pos2[1]:
        return True
    elif pos1[0] == pos2[0] and pos1[1]-1 == pos2[1]:
        return True
    elif  pos1[0] == pos2[0] and pos1[1]+1 == pos2[1]:
        return True
    elif pos1[0]+1 == pos2[0] and pos1[1] == pos2[1]:
        return True
    elif pos1[0]+1 == pos2[0] and pos1[1]+1 == pos2[1]:
        return True
    return False

# Nはノード数, Mは条件数(友達関係)
N = int(input())
UF = UnionFind(N) # ノード数で初期化
point_dict = {}
for i in range(N):
    x, y = map(int, input().split())
    point_dict[i] = (x, y)
for i in range(N):
    for j in range(N):
        if check(point_dict[i], point_dict[j]):
            # print(point_dict[i], point_dict[j])
            UF.union(i, j) # 同じ集合にする

# print(UF.parents)
print(len([val for val in UF.parents if val<0])) # 集合の要素数を取得