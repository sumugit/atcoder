N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

def minimum_operations(n, m, x_positions, a_counts):
    # 初期状態のマスと石の数をペアにし、位置の昇順でソート
    xa = sorted(zip(x_positions, a_counts))
    
    sum_stones = 0  # 現在の石の合計数
    sum_idx = 0     # 現在の位置と石の積の合計
    
    # 各マスについて確認
    for x, a in xa:
        # 必要な位置までの石が足りない場合は解決不可能
        if sum_stones < x - 1: # -1 は置く石を除く操作
            return -1
        # 石の合計と位置に対する石の積の合計を更新
        sum_stones += a
        sum_idx += a * x

    # すべてのマスに1つずつ石を置くためには、石の合計がNである必要がある
    if sum_stones != n:
        return -1
    
    # 操作回数の最小値を計算 (理想的な盤面と現在の盤面の誤差)
    return n * (n + 1) // 2 - sum_idx

ans = minimum_operations(N, M, X, A)
print(ans)