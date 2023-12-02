N, S, M, L = map(int, input().split())

def min_cost_to_buy_eggs(N, S, M, L):
    # 十分に大きな数でDPテーブルを初期化
    dp = [float('inf')] * (N + 12)
    dp[0] = 0

    # DPテーブルを更新
    for i in range(N + 12):
        if i >= 6:
            dp[i] = min(dp[i], dp[i - 6] + S)
        if i >= 8:
            dp[i] = min(dp[i], dp[i - 8] + M)
        if i >= 12:
            dp[i] = min(dp[i], dp[i - 12] + L)

    # N個以上の卵を購入するために必要な最小コストを返す
    return min(dp[N:])

# 最小コストを計算
print(min_cost_to_buy_eggs(N, S, M, L))

