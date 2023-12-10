import itertools

def count_inversions(seq):
    """ Count inversions in a sequence. """
    return sum(i < j and seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))

def main():
    h, w = map(int, input().split())
    a = [[0] * w for _ in range(h)]
    b = [[0] * w for _ in range(h)]
    
    for i in range(h):
        a[i] = list(map(int, input().split()))
    for i in range(h):
        b[i] = list(map(int, input().split()))

    p = list(range(h))
    q = list(range(w))
    
    inf = 1000000000
    ans = inf

    for p_perm in itertools.permutations(p):
        for q_perm in itertools.permutations(q):
            match = True
            for i in range(h):
                for j in range(w):
                    if a[p_perm[i]][q_perm[j]] != b[i][j]:
                        match = False
                        break
                if not match:
                    break

            if not match:
                continue
            # A == B の時
            # index (1, 2,..., h)を並び替えて index (x, y,...,z) にする時、隣接要素の並び替え総数は転倒数に等しい
            # O(N^2)
            pinv = count_inversions(p_perm)
            qinv = count_inversions(q_perm)
            ans = min(ans, pinv + qinv)
    
    print(-1 if ans == inf else ans)

if __name__ == "__main__":
    main()
