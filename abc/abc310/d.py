N, T, M = map(int, input().split())

# 一人ずつ選手を追加する操作を全探索的に試す。

# hateは各選手の嫌いな他の選手をビット列で表現したリストです。
# hate[i]のjビット目が1の場合、i番目の選手とj番目の選手の相性が悪いことを示します。
# 二次元リストを作らなくて済む賢い方法!
hate = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    hate[b-1] |= 1 << (a-1)

# dfsは深さ優先探索を行う再帰関数です。
# teamsは現在のチームの状況をビット列で表現したリストで、
# nowは現在考慮している選手のインデックスです。
def dfs(teams, now):
    # 最後の選手まで見て T チームに分かれていれば OK
    if now == N:
        return len(teams) == T

    ans = 0

    # すでにあるチームに now 番目の選手を追加する
    for i, team in enumerate(teams):
        # チームに now 番目の選手と相性の悪い選手がいなければ
        if not (team & hate[now]):
            teams[i] ^= 1 << now
            ans += dfs(teams, now + 1)
            # a ^= b は a = a ^ b と同じ (XOR)
            teams[i] ^= 1 << now

    # チーム数に余裕があるとき、新しいチームを作る
    if len(teams) < T:
        teams.append(1 << now)
        ans += dfs(teams, now + 1)
        teams.pop()

    return ans

teams = []
print(dfs(teams, 0))
