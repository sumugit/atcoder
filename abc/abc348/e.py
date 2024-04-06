def main():
    # Input
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    c = list(map(int, input().split()))
    
    # Build the tree
    tree = [[] for _ in range(n)]
    for a, b in edges:
        a -= 1
        b -= 1
        tree[a].append(b)
        tree[b].append(a)

    # DFS to calculate subtree sums
    subtree_sum_c = [0] * n
    subtree_sum_dist = [0] * n
    
    def dfs(v, par):
        for t in tree[v]:
            if t == par:
                continue
            child_sum_c, child_sum_d = dfs(t, v)
            subtree_sum_c[v] += child_sum_c
            subtree_sum_dist[v] += child_sum_d
        subtree_sum_dist[v] += subtree_sum_c[v]
        subtree_sum_c[v] += c[v]
        return subtree_sum_c[v], subtree_sum_dist[v]

    dfs(0, -1)

    # Re-rooting to calculate the answer for every node
    f = [0] * n
    
    def rerooting(v, par, par_sum_c, par_sum_dist):
        f[v] = subtree_sum_dist[v] + par_sum_dist
        for t in tree[v]:
            if t == par:
                continue
            nc = par_sum_c + subtree_sum_c[v] - subtree_sum_c[t]
            nd = par_sum_dist + subtree_sum_dist[v] - subtree_sum_dist[t] - subtree_sum_c[t] + nc
            rerooting(t, v, nc, nd)

    rerooting(0, -1, 0, 0)

    # Output the minimum value among all nodes
    print(min(f))

if __name__ == "__main__":
    main()
