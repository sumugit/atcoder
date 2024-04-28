# 最大フロー用の辺の構造体
class maxflow_edge:
	def __init__(self, to, cap, rev):
		self.to = to   # 辺の行き先
		self.cap = cap # 辺の容量 (容量は辺にかかる)
		self.rev = rev # 逆辺の行き先
        # rev については、行き先の頂点が連想配列の何番目に格納されているかを表す

# 深さ優先探索 (Step1 -- Step3 を実行するには深さ優先である必要がある)
# 理由: goal まで通るパスが1つ見つかれば良いため
def dfs(pos, goal, F, G, used):
    # Step 1 -- Step 3
	if pos == goal:
		return F # ゴールに到着：フローを流せる！
	# 探索する
	used[pos] = True
	for e in G[pos]:
		# 容量が 1 以上でかつ、まだ訪問していない頂点にのみ行く
		if e.cap > 0 and not used[e.to]:
            # 最大流量は min(F, e.cap)
			flow = dfs(e.to, goal, min(F, e.cap), G, used)
			# フローを流せる場合、残余グラフの容量を flow だけ増減させる
			if flow >= 1:
				e.cap -= flow
				G[e.to][e.rev].cap += flow
				return flow
	# すべての辺を探索しても見つからなかった場合
	return 0

#  頂点 s から頂点 t までの最大フローの総流量を返す（頂点数 N、辺のリスト edges）
def maxflow(N, s, t, edges):
	# 初期状態の残余グラフを構築
	# （ここは書籍とは少し異なる実装をしているため、8 行目は G[a] に追加された後なので len(G[a]) - 1 となっていることに注意）
	G = [ list() for i in range(N + 1) ]
	for a, b, c in edges:
		G[a].append(maxflow_edge(b, c, len(G[b])))
		G[b].append(maxflow_edge(a, 0, len(G[a]) - 1))
	INF = 10 ** 10
	total_flow = 0
	while True:
        # goal までに残量>0のみのパスがある限り繰り返す
		used = [ False ] * (N + 1)
        # Ford-Fulkerson 法の Step 1 -- Step3
		F = dfs(s, t, INF, G, used)
		if F > 0:
			total_flow += F
		else:
			break # フローを流せなくなったら、操作終了
	return total_flow

# 入力
N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 答えを求めて出力
answer = maxflow(N, 1, N, edges)
print(answer)