N, Q = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(Q)]

# UnionFind木だと連結成分は抽出できるが、順路は得られない
# ダブリングで解く
# dp[i][j] := 穴jにいる時，2^i日後どこの穴にいるか
dp = [[-1]*(N) for _ in range(30)]
dp[0] = [a-1 for a in A]

for i in range(1, 30):
    for j in range(N):
        dp[i][j] = dp[i-1][dp[i-1][j]]

for x, y in XY:
    x -= 1
    for i in range(30):
        # 大きい桁から見るため右シフト
        if (y >> i) & 1:
            x = dp[i][x]

    print(x+1)