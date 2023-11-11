from itertools import combinations

# 全域木になっているかを判定するためにUnionFindを使う
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent, rank):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1
        return True
    return False


def main():
    N, M, K = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    min_cost = K
    num_edges = N - 1
    for subset in combinations(edges, num_edges):
        parent = list(range(N))
        rank = [0] * N
        cost = 0
        for u, v, w in subset:
            if union(u - 1, v - 1, parent, rank):
                cost += w % K
        if all(find(i, parent) == find(0, parent) for i in range(N)):
            min_cost = min(min_cost, cost % K)

    print(min_cost)


main()
